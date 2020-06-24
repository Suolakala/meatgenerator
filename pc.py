from randomizer import random_good_traits
import random


class PlayerCharacter:
    def __init__(self):
        """
        Creates random player character.
        """
        self.stats = {}
        self.name = "Maggarakeisari"
        self.generate_stats()
        self.background = random_good_traits()
        self.update_traits_to_stats()

    def generate_stats(self):
        self.generate_basic_stats()

    def add_stat(self, stat):
        new_key = {stat.shortdesc:stat}
        self.stats.update(new_key)

    def generate_basic_stats(self):
        self.add_stat(Stat("Kunto", "KUN"))
        self.add_stat(Stat("Koko", "KOK"))
        self.add_stat(Stat("Ketteryys", "KET"))
        self.add_stat(Stat("Äly", "ALY"))
        self.add_stat(Stat("Viisaus", "VII"))
        self.add_stat(Stat("Vetovoima", "VET"))
        self.add_stat(Stat("Koulutus", "KOU"))
        self.add_stat(Stat("Koulutus", "KOU"))

    def update_traits_to_stats(self):
        """
        Updates possible effect of each trait to character
        :return:
        """
        for trait in self.background:
            if trait.effect_to_stats:
                for effect in trait.effect_to_stats:
                    updated_value = self.stats[effect].number + trait.effect_to_stats[effect]
                    if updated_value < 0:
                        updated_value = 0
                    self.stats[effect].number = updated_value
                    print("added {} to stats".format(trait.name))


class Stat:
    def __init__(self, description, shortdesc, number="random_basic_stat"):
        self.description = description
        self.shortdesc = shortdesc
        if number == "random_basic_stat":
            d1 = random.randint(1, 6)
            d2 = random.randint(1, 6)
            d3 = random.randint(1, 6)
            d4 = random.randint(1, 6)
            self.number = d1+d2+d3+d4-3
        if description is not "Koulutus" and self.number < 3:
            self.number = 3
