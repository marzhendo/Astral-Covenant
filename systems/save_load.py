import json
import os
from data.servants import create_artoria, create_emiya, create_mash
from core.player import Player
SERVANT_FACTORY = {
    "Artoria Pendragon": create_artoria,
    "Emiya": create_emiya,
    "Mash Kyrielight": create_mash
}



def servant_to_dict(s):
    return {
        "name": s.name,
        "hp": s.hp,
        "max_hp": s.max_hp,
        "attack": s.attack,
        "defense": s.defense,
        "mana": s.mana,
        "max_mana": s.max_mana,
        "bond": s.bond,
        "level": s.level,
        "exp": s.exp,
        "exp_to_next": s.exp_to_next,
        "cooldown": s.cooldown
    }

def player_to_dict(player):

    return {
        "name": player.name,
        "hp": player.hp,
        "max_hp": player.max_hp,
        "attack": player.attack,
        "defense": player.defense,
        "mana": player.mana,
        "max_mana": player.max_mana,
        "level": player.level,
        "exp": player.exp,
        "exp_to_next": player.exp_to_next,
        "gold": player.gold,

        "active_servant": player.active_servant.name if player.active_servant else None,

        "servants": [servant_to_dict(s) for s in player.servants]
    }

def save_game(player, slot="slot1"):

    os.makedirs("saves", exist_ok=True)

    data = player_to_dict(player)

    with open(f"saves/{slot}.json", "w") as f:
        json.dump(data, f, indent=4)

    print(f"Game saved to {slot}.json")

def load_game(slot="slot1"):

    path = f"saves/{slot}.json"

    if not os.path.exists(path):
        print("Save file not found.")
        return None

    with open(path, "r") as f:
        data = json.load(f)

    player = Player(data["name"])

    # restore player stats
    player.hp = data["hp"]
    player.max_hp = data["max_hp"]
    player.attack = data["attack"]
    player.defense = data["defense"]
    player.mana = data["mana"]
    player.max_mana = data["max_mana"]
    player.level = data["level"]
    player.exp = data["exp"]
    player.exp_to_next = data["exp_to_next"]
    player.gold = data["gold"]

    # restore servants
    for sdata in data["servants"]:

        name = sdata["name"]

        if name not in SERVANT_FACTORY:
            continue

        s = SERVANT_FACTORY[name]()

        s.hp = sdata["hp"]
        s.max_hp = sdata["max_hp"]
        s.attack = sdata["attack"]
        s.defense = sdata["defense"]
        s.mana = sdata["mana"]
        s.max_mana = sdata["max_mana"]
        s.bond = sdata["bond"]
        s.level = sdata["level"]
        s.exp = sdata["exp"]
        s.exp_to_next = sdata["exp_to_next"]
        s.cooldown = sdata["cooldown"]

        player.servants.append(s)

        if s.name == data["active_servant"]:
            player.active_servant = s

    print("Game loaded successfully.")
    return player