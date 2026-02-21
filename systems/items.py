def use_item(player, item_name):

    if item_name not in player.inventory or player.inventory[item_name] <= 0:
        print("You don't have that item.")
        return False

    # ----- HP POTION -----
    if item_name == "Potion":
        heal = int(player.max_hp * 0.4)
        player.hp = min(player.max_hp, player.hp + heal)
        print(f"You recover {heal} HP!")

    # ----- MANA POTION -----
    elif item_name == "Mana Potion":
        mana = int(player.max_mana * 0.4)
        player.mana = min(player.max_mana, player.mana + mana)
        print(f"You recover {mana} Mana!")

    else:
        print("Item not usable.")
        return False

    player.inventory[item_name] -= 1
    return True