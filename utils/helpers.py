def show_hud(player):

    servant = player.active_servant

    print("\n----------------------------")
    print(f"{player.name} HP:{player.hp}/{player.max_hp} | Mana:{player.mana}/{player.max_mana}")

    if servant:
        print(f"{servant.name} HP:{servant.hp}/{servant.max_hp} | Mana:{servant.mana}/{servant.max_mana}")

    print("----------------------------")