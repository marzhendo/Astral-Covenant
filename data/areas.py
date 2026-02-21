import random
from core.enemy import Enemy

def whispering_woods_enemy():
    pool = [
        Enemy("Slime", 28, 7, 2, exp_reward=18),
        Enemy("Goblin", 32, 8, 3, exp_reward=22),
        Enemy("Wolf", 30, 9, 2, exp_reward=24)
    ]

    # chance multi enemy kecil di early
    if random.random() < 0.25:
        return random.sample(pool, k=2)
    else:
        return [random.choice(pool)]


AREAS = {
    "1": {
        "name": "Whispering Woods",
        "recommended": "Lv 1-3",
        "encounter_func": whispering_woods_enemy
    }
}