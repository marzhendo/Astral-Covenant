import random
from utils.colors import C
from utils.ui import bar, show_player_hud, clear
from core import player
from systems.items import use_item

# ======================
# BATTLE LOG BUFFER
# ======================
battle_log = []
LOG_LIMIT = 10

def log(msg):
    battle_log.append(msg)
    if len(battle_log) > LOG_LIMIT:
        battle_log.pop(0)


def render_screen(player):
    clear()
    print("="*42)
    show_player_hud(player)
    print("="*42)

    for line in battle_log:
        print(line)

    print("="*42)

# ======================
# DAMAGE CALCULATION
# ======================

def calc_damage(attacker, defender):

    defense = defender.defense

    if defender.has_status("Defense Down"):
        defense *= 0.7

    base = attacker.attack - (defense * 0.4)

    import random
    variance = random.uniform(0.7, 1.4)
    dmg = max(1, int(base * variance))

    # astral mark = bonus damage taken
    if defender.has_status("Astral Mark"):
        dmg = int(dmg * 1.15)

    # crit
    if random.random() < 0.15:
        crit_mult = random.uniform(1.8, 2.5)
        dmg = int(dmg * crit_mult)
        print(C.YELLOW + "⚡ CRITICAL STRIKE!" + C.RESET)

    return dmg


# ======================
# MANA HANDLING
# ======================

def spend_mana_with_transfer(servant, player, cost):
    """
    Use servant mana first.
    If not enough, pull remaining from player with penalty.
    Returns True if skill can be used.
    """

    if servant.mana >= cost:
        servant.mana -= cost
        return True

    # need transfer
    remaining = cost - servant.mana
    servant.mana = 0

    # inefficiency based on bond
    penalty = 1.3 - (servant.bond * 0.05)
    penalty = max(1.0, penalty)  # never cheaper than normal

    transfer_cost = int(remaining * penalty)

    if player.mana >= transfer_cost:
        player.mana -= transfer_cost
        print(f"{servant.name} draws {transfer_cost} mana from you!")
        return True

    print("Not enough mana for servant skill!")
    return False


# ======================
# PLAYER TURN
# ======================

def player_turn(player, enemies):

    if player.has_status("Stun"):
        print("You are stunned and cannot act!")
        return False

    servant = player.active_servant

    while True:
        print("\n== Your Turn ==")
        print("1. Attack")
        print("2. Command Servant Skill")
        print("3. Use Item")
        print("4. Check Status")

        choice = input("> ")

        # ----- BASIC ATTACK -----
        if choice == "1":
            target = choose_target(enemies)
            dmg = calc_damage(player, target)
            target.hp -= dmg
            print(f"{C.GREEN}{player.name}{C.RESET} deals {C.RED}{dmg}{C.RESET} damage to {target.name}")
            return False   # servant skill NOT used

        # ----- SERVANT SKILL -----
        elif choice == "2":

            if not servant:
                print("No active servant.")
                continue

            if servant.cooldown > 0:
                print(f"Skill on cooldown ({servant.cooldown} turns left)")
                continue

            print(f"Use {servant.skill_name}? (cost {servant.skill_cost}) Y/N")
            confirm = input("> ").lower()

            if confirm != "y":
                continue

            # mana check
            if not spend_mana_with_transfer(servant, player, servant.skill_cost):
                continue

            # choose target
            target = choose_target(enemies)

            # skill damage = stronger than basic
            dmg = int(calc_damage(servant, target) * 1.5)
            target.hp -= dmg

            print(f"{servant.name} uses {servant.skill_name}!")
            print(f"{C.GREEN}{servant.name}{C.RESET} deals {C.RED}{dmg}{C.RESET} damage to {target.name}")

            servant.cooldown = servant.cooldown_max
            return True   # servant skill used

        # ----- USE ITEM -----
        elif choice == "3":

            if not player.inventory:
                print("Inventory empty.")
                continue

            print("\nInventory:")
            items = [k for k,v in player.inventory.items() if v > 0]

            for i, name in enumerate(items):
                print(f"{i+1}. {name} x{player.inventory[name]}")

            pick = int(input("> ")) - 1

            if 0 <= pick < len(items):
                used = use_item(player, items[pick])
                if used:
                    return False
        # ----- STATUS -----
        elif choice == "4":
            show_combat_status(player, enemies)

        else:
                print("Invalid choice.")


# ======================
# TARGET SELECTION
# ======================

def choose_target(enemies):
    alive = [e for e in enemies if e.is_alive()]

    while True:
        print("\nChoose target:")
        for i, e in enumerate(alive):
            print(f"{i+1}. {e.name} HP:{e.hp}")

        idx = int(input("> ")) - 1
        if 0 <= idx < len(alive):
            return alive[idx]


# ======================
# SERVANT AUTO ATTACK
# ======================

def servant_auto_attack(servant, enemies, player):
    if servant and servant.has_status("Stun"):
        print(f"{servant.name} is stunned!")
        return
    if not servant or not servant.is_alive():
        return

    alive = [e for e in enemies if e.is_alive()]
    if not alive:
        return

    target = random.choice(alive)
    servant.skill_func(servant, player, enemies, calc_damage, print)

    print(f"{servant.name} attacks {target.name} for {calc_damage(servant, target)} damage.")


# ======================
# ENEMY TURN
# ======================

def enemy_turn(player, servant, enemies):

    for e in enemies:
        if not e.is_alive():
            continue
        if e.has_status("Stun"):
            print(f"{e.name} is stunned!")
            continue

        possible_targets = [player]
        if servant and servant.is_alive():
            possible_targets.append(servant)

        target = random.choice(possible_targets)

        dmg = calc_damage(e, target)
        target.hp -= dmg

        print(f"{C.GREEN}{e.name}{C.RESET} deals {C.RED}{dmg}{C.RESET} damage to {target.name}")


# ======================
# END TURN UPDATES
# ======================

def end_turn_updates(player, enemies):

    # regen
    player.mana = min(player.max_mana, player.mana + 3)

    servant = player.active_servant
    if servant:
        servant.mana = min(servant.max_mana, servant.mana + 2)
        if servant.cooldown > 0:
            servant.cooldown -= 1

    # process statuses
    process_status(player)
    if servant:
        process_status(servant)

    for e in enemies:
        process_status(e)


# ======================
# STATUS DISPLAY
# ======================

def show_combat_status(player, enemies):

    print(C.BOLD + "\n-- PLAYER TURN --" + C.RESET)
    print(f"{player.name} HP:{player.hp}/{player.max_hp} Mana:{player.mana}")

    if player.active_servant:
        s = player.active_servant
        print(f"\n--- SERVANT ---")
        print(f"{s.name} HP:{s.hp}/{s.max_hp} Mana:{s.mana}")
        print(f"Cooldown:{s.cooldown}")

    print(C.BOLD + "\n-- ENEMY TURN --" + C.RESET)
    for e in enemies:
        print(f"{e.name} HP:{e.hp}")

def try_apply_status(target, name, duration, chance):
    import random
    if random.random() < chance:
        target.add_status(name, duration)
        print(f"{target.name} is affected by {name}!")
        


# ======================
# MAIN BATTLE LOOP
# ======================

def run_battle(player, enemies):
    

    servant = player.active_servant

    print("\n=== BATTLE START ===")

    while player.is_alive() and any(e.is_alive() for e in enemies):
        clear()
        show_player_hud(player)

        # PLAYER TURN
        print(C.BOLD + "\n-- PLAYER TURN --" + C.RESET)
        servant_skill_used = player_turn(player, enemies)

        # remove dead enemies
        enemies = [e for e in enemies if e.is_alive()]
        if not enemies:
            break

        # SERVANT AUTO ATTACK
        if not servant_skill_used:
            servant_auto_attack(servant, enemies, player)

        # ENEMY TURN
        print(C.BOLD + "\n-- ENEMY TURN --" + C.RESET)
        enemy_turn(player, servant, enemies)

        # END TURN
        end_turn_updates(player, enemies)

    # RESULT
    if player.is_alive():

        total_exp = sum(e.exp_reward for e in enemies)

        print(C.GREEN + f"\nVICTORY! Gained {total_exp} EXP" + C.RESET)

        if random.random() < 0.25:
            player.inventory["Potion"] = player.inventory.get("Potion",0) + 1
            print("You found a Potion!")
        

        player.gain_exp(total_exp)
        print(f"{player.name} Lv{player.level} HP:{player.hp}/{player.max_hp} Mana:{player.mana}")

    if player.active_servant:
        player.active_servant.gain_exp(int(total_exp * 0.8))
        print(f"{servant.name} Lv{servant.level} HP:{servant.hp}/{servant.max_hp} Mana:{servant.mana}")
        return True
    else:
        print(C.RED + "\nDEFEAT..." + C.RESET)
        return False

def process_status(entity):

    for s in entity.status_effects[:]:

        name = s["name"]

        # ----- BURN -----
        if name == "Burn":
            dmg = max(1, int(entity.max_hp * 0.05))
            entity.hp -= dmg
            print(C.MAGENTA + f"{entity.name} is burning!" + C.RESET)

        # ----- POISON -----
        elif name == "Poison":
            dmg = 3
            entity.hp -= dmg
            print(C.MAGENTA + f"{entity.name} is poisoned!" + C.RESET)

        # defense down handled in damage calc
        # stun handled in turn logic

        # reduce duration
        s["duration"] -= 1
        if s["duration"] <= 0:
            entity.status_effects.remove(s)
            print(f"{entity.name} is no longer affected by {name}.")
    