from traits import *
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
        self.printchar()

    def printchar(self):
        print("Created char: {}".format(self.name))
        for trait in self.background:
            print(trait.name)
        print_stats(self.stats)

    def generate_stats(self):
        self.generate_basic_stats()

    def generate_basic_stats(self):
        basic_stats = {
            "KUN": Stat("Kunto"),
            "KOK": Stat("Koko"),
            "KET": Stat("Ketteryys"),
            "ALY": Stat("Äly"),
            "VII": Stat("Viisaus"),
            "TAH": Stat("Tahdonvoima"),
            "VET": Stat("Vetovoima"),
            "KOU": Stat("Koulutus"),
            "ONN": Stat("Onnekkuus")
        }
        self.stats.update(basic_stats)

    def update_traits_to_stats(self):
        """
        Updates possible effect of each trait to character
        :return:
        """
        print(self.background)
        for trait in self.background:
            if trait.effect_to_stats:
                for effect in trait.effect_to_stats:
                    updated_value = self.stats[effect].number + trait.effect_to_stats[effect]
                    if updated_value < 0:
                        updated_value = 0
                    self.stats[effect].number = updated_value
                    print("added {} to stats".format(trait.name))


class Stat:
    def __init__(self, description, number="random"):
        self.description = description
        if number == "random":
            d1 = random.randint(1, 6)
            d2 = random.randint(1, 6)
            d3 = random.randint(1, 6)
            d4 = random.randint(1, 6)
            self.number = d1+d2+d3+d4-3
        if description is not "Koulutus" and self.number < 3:
            self.number = 3


def print_stats(list_of_stats):
    for stat in list_of_stats:
        print("{}:{}".format(list_of_stats[stat].description, list_of_stats[stat].number))