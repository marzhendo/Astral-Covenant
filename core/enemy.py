from core.entity import Entity

class Enemy(Entity):
    def __init__(self, name, hp, attack, defense, mana=0, exp_reward=25):
        super().__init__(name, hp, attack, defense, mana)
        self.exp_reward = exp_reward