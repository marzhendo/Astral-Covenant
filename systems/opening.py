from core.enemy import Enemy
from systems.battle import run_battle
from data.servants import create_artoria, create_emiya, create_mash


def prologue_scene():
    print("\nThe sky fractures...")
    input()
    print("A crimson rift tears open above the plains.")
    input()
    print("Creatures descend from the Astral Abyss.")
    input()
    print("You are no hero. Just someone in the wrong place.")
    input()
    print("\nA Rift Beast notices you.\n")

def scripted_loss_battle(player):

    print("\n=== FIRST ENCOUNTER ===")

    # beast terlalu kuat
    beast = Enemy("Rift Beast", hp=120, attack=25, defense=10)

    # run normal battle
    result = run_battle(player, [beast])

    # walaupun menang karena RNG aneh, tetap paksa kalah
    player.hp = 0
    print("\nYou collapse...")

def awakening_scene():
    print("\nDarkness surrounds you.")
    input()
    print("A sigil ignites beneath your body.")
    input()
    print("Three voices answer your call...\n")

def choose_servant():

    print("1. Artoria Pendragon – The Radiant Saber")
    print("2. Emiya – The Phantom Archer")
    print("3. Mash Kyrielight – The Shield of Resolve")

    while True:
        choice = input("\nChoose your covenant: ")

        if choice == "1":
            servant = create_artoria()
            break
        elif choice == "2":
            servant = create_emiya()
            break
        elif choice == "3":
            servant = create_mash()
            break
        else:
            print("Invalid choice.")

    print(f"\nCOVENANT FORMED WITH {servant.name}!\n")
    return servant

def restore_after_summon(player, servant):

    player.hp = player.max_hp
    player.mana = player.max_mana

    servant.hp = servant.max_hp
    servant.mana = servant.max_mana

    player.servants.append(servant)
    player.active_servant = servant

def tutorial_battle(player):

    print("\nA Rift Beast approaches again...")
    print("But this time, you are not alone.\n")

    beast = Enemy("Rift Beast", hp=45, attack=10, defense=4)

    run_battle(player, [beast])

    print("\nThe beast dissolves into astral dust.")
    print("You survived your first true battle.")

def run_opening(player):

    prologue_scene()
    scripted_loss_battle(player)
    awakening_scene()

    servant = choose_servant()
    restore_after_summon(player, servant)

    tutorial_battle(player)

