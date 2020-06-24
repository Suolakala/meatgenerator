from randomizer import random_good_traits
import random
import os


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
        self.print_char()

    def print_char(self, format="console"):
         if format == "console":
            print("Created char: {}".format(self.name))
            for trait in self.background:
                print(trait.name)
            print_stats(self.stats)
         elif format == "textfile":
            self.print_char_to_txt()

         else:
            raise Exception("Format not supported, supported printing:\nconsole\ntextfile")

    def print_char_to_txt(self):
        script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
        rel_path = "created_chars\\{}.txt".format(self.name)
        abs_file_path = os.path.join(script_dir, rel_path)
        print(abs_file_path)
        text_file = open(abs_file_path, "w")
        text_file.write("{}\n".format(self.name))
        for stat in self.stats:
            text_file.write("{}:{}\n".format(self.stats[stat].description, str(self.stats[stat].number)))

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


def print_stats(list_of_stats):
    for stat in list_of_stats:
        print("{}:{}".format(list_of_stats[stat].description, list_of_stats[stat].number))
