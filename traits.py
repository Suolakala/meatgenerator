class Trait:
    def __init__(self, name, desc="TODO"):
        self.name = name
        self.desc = desc
        self.effect_to_stats = {}

    def add_effect_to_trait(self, stat, value):
        #TODO check that value is valid stat
        self.effect_to_stats[stat] = value