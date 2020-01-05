#!/usr/bin/python

import sys
from randomizer import random_good_traits

error_string = "Did not get command. List of commands:\n" \
               "traits <amount of traits, optional>. Usage: chargen.py traits 1\n" \
               "newpc"

if len(sys.argv) == 1:
    print(error_string)
    exit(0)

if sys.argv[1] == "traits":
    list_good_traits = []
    if len(sys.argv) == 2:
        list_good_traits = random_good_traits()
    else:
        list_good_traits = random_good_traits(int(sys.argv[2]))
    print("Following good traits were chosen: ")
    for trait in list_good_traits:
        print("{} - {}".format(trait.name, trait.desc))
elif sys.argv[1] == "background":
    print("TODO this command is not implemented :D")
elif sys.argv[1] == "npc":
    print("TODO this command is not implemented :D")
elif sys.argv[1] == "newpc":
    print("Oispa kaljaa :D")
else:
    print(error_string)
