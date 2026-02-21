import random

def artoria_skill(servant, player, enemies, calc_damage, try_apply_status):

    print(f"{servant.name} unleashes EXCALIBUR!")

    for e in enemies:
        if not e.is_alive():
            continue

        dmg = int(calc_damage(servant, e) * 1.4)
        e.hp -= dmg
        print(f"{e.name} takes {dmg} damage!")

        # 30% defense down
        try_apply_status(e, "Defense Down", 2, 0.3)
def emiya_skill(servant, player, enemies, calc_damage, try_apply_status):

    print(f"{servant.name} fires Broken Phantasm!")

    hits = random.randint(2,4)

    for _ in range(hits):
        alive = [e for e in enemies if e.is_alive()]
        if not alive:
            return

        target = random.choice(alive)

        dmg = int(calc_damage(servant, target) * 0.9)
        target.hp -= dmg
        print(f"Arrow hits {target.name} for {dmg}!")

        # 25% burn
        try_apply_status(target, "Burn", 2, 0.25)

def mash_skill(servant, player, enemies, calc_damage, try_apply_status):

    print(f"{servant.name} raises Lord Chaldeas!")

    # reduce damage via Astral Mark removal / defensive buff simulation
    if player.has_status("Defense Down"):
        player.status_effects = [
            s for s in player.status_effects if s["name"] != "Defense Down"
        ]
        print("Defense restored!")

    heal = int(player.max_hp * 0.25)
    player.hp = min(player.max_hp, player.hp + heal)

    print(f"{player.name} recovers {heal} HP!")