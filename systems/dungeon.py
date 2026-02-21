from systems.battle import run_battle
from data.dungeons import DUNGEONS


def dungeon_menu(player):
    while True:
        print("\n=== DUNGEONS ===")

        for key, d in DUNGEONS.items():
            print(f"{key}. {d['name']} ({d['recommended']})")

        print("0. Back")

        choice = input("> ")

        if choice == "0":
            return

        if choice not in DUNGEONS:
            print("Invalid choice.")
            continue

        run_dungeon(player, DUNGEONS[choice])

def run_dungeon(player, dungeon):

    print(f"\nEntering {dungeon['name']}...")
    print("You cannot rest inside the dungeon.\n")

    print(f"\n{player.name} HP:{player.hp}/{player.max_hp} Mana:{player.mana}")
    if player.active_servant:
        s = player.active_servant
    print(f"{s.name} HP:{s.hp}/{s.max_hp} Mana:{s.mana}")
    waves = dungeon["waves_func"]()

    for i, wave in enumerate(waves):

        # miniboss check
        if i == len(waves) - 1:
            print("\n🔥 A powerful presence appears...")
            print("MINIBOSS WAVE!")
        else:
            print(f"\n--- Wave {i+1} ---")

        # encounter text
        if len(wave) == 1:
            print(f"You've encountered {wave[0].name}!")
        else:
            names = ", ".join(e.name for e in wave)
            print(f"You've encountered: {names}")

        # battle
        result = run_battle(player, wave)

        if not result:
            print("\nYou were defeated and forced to retreat...")
            player.hp = 1
            return

    print("\n🏆 Dungeon Cleared!")