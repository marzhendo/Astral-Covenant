from systems.save_load import load_game
from systems.opening import run_opening
from systems.town import town_loop
from core.player import Player


def main():

    print("=== ASTRAL COVENANT ===")
    print("1. New Game")
    print("2. Load Game")

    choice = input("> ")

    if choice == "2":
        player = load_game()
        if player:
            town_loop(player)
            return

    # new game
    name = input("Enter your name: ")
    player = Player(name)

    run_opening(player)
    town_loop(player)

if __name__ == "__main__":
    main()