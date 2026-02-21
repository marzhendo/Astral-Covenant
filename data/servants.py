from core.servant import Servant
from systems.skills import artoria_skill, emiya_skill, mash_skill

def create_artoria():
    return Servant(
        "Artoria Pendragon",
        85,16,10,32,
        "Excalibur",
        20,
        3,
        artoria_skill
    )

def create_emiya():
    return Servant(
        "Emiya",
        75,17,8,36,
        "Broken Phantasm",
        22,
        3,
        emiya_skill
    )

def create_mash():
    return Servant(
        "Mash Kyrielight",
        100,12,15,40,
        "Lord Chaldeas",
        18,
        4,
        mash_skill
    )