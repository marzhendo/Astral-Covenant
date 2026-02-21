class Entity:
    def __init__(self, name, hp, attack, defense, mana=0):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.max_mana = mana
        self.mana = mana
        self.status_effects = []

    def is_alive(self):
        return self.hp > 0

    # ---- STATUS HELPERS ----
    def has_status(self, name):
        return any(s["name"] == name for s in self.status_effects)

    def add_status(self, name, duration):
        # refresh if already exists
        for s in self.status_effects:
            if s["name"] == name:
                s["duration"] = duration
                return

        # max 2 status
        if len(self.status_effects) >= 2:
            self.status_effects.pop(0)

        self.status_effects.append({"name": name, "duration": duration})