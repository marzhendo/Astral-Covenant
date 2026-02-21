from core.entity import Entity

class Servant(Entity):
    def __init__(self, name, hp, attack, defense, mana,
                 skill_name, skill_cost, cooldown, skill_func):

        super().__init__(name, hp, attack, defense, mana)

        self.skill_name = skill_name
        self.skill_cost = skill_cost
        self.cooldown_max = cooldown
        self.cooldown = 0
        self.skill_func = skill_func

        self.bond = 1

        # LEVEL SYSTEM
        self.level = 1
        self.exp = 0
        self.exp_to_next = 80


    def gain_exp(self, amount):
        self.exp += amount

        while self.exp >= self.exp_to_next:
            self.exp -= self.exp_to_next
            self.level_up()


    def level_up(self):
        self.level += 1
        self.exp_to_next = int(80 * (self.level ** 1.5))

        self.max_hp += 8
        self.attack += 2
        self.defense += 1
        self.max_mana += 3

        self.hp = self.max_hp
        self.mana = self.max_mana

        print(f"{self.name} reached Level {self.level}!")