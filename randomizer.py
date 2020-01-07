import random
from list_of_traits import list_of_good_traits


def random_good_traits(number=2):
    list_good_traits = random.sample(list_of_good_traits, k=number)
    return list_good_traits
