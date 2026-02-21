from systems.battle import run_battle
from systems.area import explore_area
from core.enemy import Enemy
from systems.save_load import save_game
def town_loop(player):

    while True:
        print("\n=== ASTRAL FRONTIER ===")
        print("1. Explore Area")
        print("2. Status")
        print("3. Rest")
        print("4. Exit")
        print("5. Save Game")

        choice = input("> ")

        if choice == "1":
            explore_area(player)

        elif choice == "2":
            show_status(player)

        elif choice == "3":
            rest(player)

        elif choice == "4":
            break
        elif choice == "5":
            save_game(player)


def show_status(player):
    print(f"\n{player.name} HP:{player.hp}/{player.max_hp}")
    if player.active_servant:
        s = player.active_servant
        print(f"Servant: {s.name} HP:{s.hp}/{s.max_hp}")


def rest(player):
    player.hp = player.max_hp
    player.mana = player.max_mana
    if player.active_servant:
        s = player.active_servant
        s.hp = s.max_hp
        s.mana = s.max_mana

    print("You feel restored.")