import traits
import random

class PlayerCharacter:
    def __init__(self):
        """
        Creates random player character.
        """
        self.stats = {
            "KUN": Stat("Kunto"),
            "KOK": Stat("Koko"),
            "KET": Stat("Ketteryys"),
            "ALY": Stat("Äly"),
            "VII": Stat("Viisaus"),
            "TAH": Stat("Tahdonvoima"),
            "VET": Stat("Vetovoima"),
            "KOU": Stat("Koulutus"),
            "ONN": Stat("Onnekkuus",
        }
        self.background = generate




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
