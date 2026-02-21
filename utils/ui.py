from utils.colors import C
import os
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def bar(current, maximum, length=20, color=C.GREEN):

    ratio = current / maximum if maximum > 0 else 0
    filled = int(length * ratio)
    empty = length - filled

    return f"{color}[{'█'*filled}{'-'*empty}]{C.RESET} {current}/{maximum}"

def show_player_hud(player):

    print(f"{C.BOLD}{player.name} Lv{player.level}{C.RESET}")
    print("HP  ", bar(player.hp, player.max_hp, color=C.RED))
    print("Mana", bar(player.mana, player.max_mana, color=C.BLUE))

    s = player.active_servant
    if s:
        print(f"\n{C.CYAN}{s.name} Lv{s.level}{C.RESET}")
        print("HP  ", bar(s.hp, s.max_hp, color=C.RED))
        print("Mana", bar(s.mana, s.max_mana, color=C.BLUE))