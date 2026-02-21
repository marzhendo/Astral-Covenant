from core.entity import Entity

class Player(Entity):
    def __init__(self, name):
        super().__init__(name, hp=80, attack=12, defense=8, mana=30)

        self.level = 1
        self.exp = 0
        self.exp_to_next = 100

        self.servants = []
        self.active_servant = None
        self.gold = 0
        self.inventory = { 
                            "Potion": 3,
                            "Mana Potion": 2
                        }


    def gain_exp(self, amount):
        print(f"\nYou gained {amount} EXP!")
        self.exp += amount

        while self.exp >= self.exp_to_next:
            self.exp -= self.exp_to_next
            self.level_up()


    def level_up(self):
        self.level += 1
        self.exp_to_next = int(100 * (self.level ** 1.5))

        # stat growth
        self.max_hp += 12
        self.attack += 2
        self.defense += 1
        self.max_mana += 4

        # heal on level
        self.hp = self.max_hp
        self.mana = self.max_mana

        print(f"\n🌟 LEVEL UP! You are now Level {self.level}!")