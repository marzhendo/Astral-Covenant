import time
import os


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


TITLE = r"""
     █████╗ ███████╗████████╗██████╗  █████╗ ██╗     
    ██╔══██╗██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██║     
    ███████║███████╗   ██║   ██████╔╝███████║██║     
    ██╔══██║╚════██║   ██║   ██╔══██╗██╔══██║██║     
    ██║  ██║███████║   ██║   ██║  ██║██║  ██║███████╗
    ╚═╝  ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝

██████╗  ██████╗ ██╗   ██╗███████╗███╗   ██╗ █████╗ ███╗   ██╗████████╗
██╔════╝ ██╔═══██╗██║   ██║██╔════╝████╗  ██║██╔══██╗████╗  ██║╚══██╔══╝
██║      ██║   ██║██║   ██║█████╗  ██╔██╗ ██║███████║██╔██╗ ██║   ██║   
██║      ██║   ██║╚██╗ ██╔╝██╔══╝  ██║╚██╗██║██╔══██║██║╚██╗██║   ██║   
╚██████╗ ╚██████╔╝ ╚████╔╝ ███████╗██║ ╚████║██║  ██║██║ ╚████║   ██║   
 ╚═════╝  ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝

                ✦ ASTRAL COVENANT ✦
"""


def show_title():
    clear()
    print(TITLE)
    print("\n        Press ENTER to begin...")
    input()

def type_text(text, delay=0.03):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()

def intro_cinematic():
    clear()

    type_text("In an age where the sky itself has begun to fracture...", 0.04)
    time.sleep(0.6)

    type_text("Rifts to the Astral Realm tear open across the world.", 0.04)
    time.sleep(0.6)

    type_text("From them emerge creatures beyond mortal understanding.", 0.04)
    time.sleep(0.6)

    type_text("\nOnly those who forge a Covenant with astral heroes can resist.", 0.045)
    time.sleep(0.8)

    type_text("\nAnd tonight...", 0.05)
    time.sleep(0.6)

    type_text("your fate begins.", 0.06)

    print("\n(Press ENTER)")
    input()

def main_menu():

    while True:
        clear()
        print(TITLE)
        print("\n" + "-"*40)
        print("1. New Game")
        print("2. Load Game")
        print("3. Exit")
        print("-"*40)

        choice = input("> ")

        if choice in ["1", "2", "3"]:
            return choice