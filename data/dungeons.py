from core.enemy import Enemy

def shadow_rift_waves():

    wave1 = [
        Enemy("Rift Slime", 30, 8, 2, exp_reward=18),
        Enemy("Rift Slime", 30, 8, 2, exp_reward=18),
    ]

    wave2 = [
        Enemy("Goblin Raider", 35, 9, 3, exp_reward=22),
        Enemy("Wolf", 32, 10, 2, exp_reward=24),
    ]

    miniboss = [
        Enemy("Abyss Goblin Chief", 70, 13, 5, exp_reward=60)
    ]

    return [wave1, wave2, miniboss]


DUNGEONS = {
    "1": {
        "name": "Shadow Rift",
        "recommended": "Lv 2+",
        "waves_func": shadow_rift_waves
    }
}