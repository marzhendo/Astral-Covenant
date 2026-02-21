import random
from systems.battle import run_battle
from data.areas import AREAS
from utils.helpers import show_hud


def explore_area(player):

    while True:
        print("\n=== SELECT AREA ===")
        for key, area in AREAS.items():
            print(f"{key}. {area['name']} ({area['recommended']})")

        print("0. Back")
        choice = input("> ")

        if choice == "0":
            return

        if choice not in AREAS:
            print("Invalid.")
            continue

        run_exploration(player, AREAS[choice])
    
def run_exploration(player, area):

    print(f"\nEntering {area['name']}...")
    print("Type 'q' to return to town.\n")

    steps = 0

    while True:

        # simple HUD each step
        show_hud(player)

        cmd = input("Press ENTER to move, or q to leave: ")
        if cmd.lower() == "q":
            print("Returning to town...")
            return

        steps += 1

        # encounter chance
        if random.random() < 0.45:
            enemies = area["encounter_func"]()

            # encounter text
            if len(enemies) == 1:
                print(f"\n⚔ You've encountered a {enemies[0].name}!")
            else:
                names = ", ".join(e.name for e in enemies)
                print(f"\n⚔ You've encountered: {names}!")

            run_battle(player, enemies)

            if not player.is_alive():
                print("You barely escape and are returned to town...")
                player.hp = 1
                return