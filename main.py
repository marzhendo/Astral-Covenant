from utils.title import show_title, intro_cinematic, main_menu
from systems.save_load import load_game
from systems.opening import run_opening
from systems.town import town_loop
from core.player import Player


def main():
    show_title()
    intro_cinematic()

    choice = main_menu()

    # LOAD GAME
    if choice == "2":
        player = load_game()
        if player:
            town_loop(player)
        return

    # EXIT
    if choice == "3":
        print("Farewell, Invoker.")
        return

    # NEW GAME
    name = input("Enter your name: ")
    player = Player(name)

    run_opening(player)
    town_loop(player)

if __name__ == "__main__":
    main()