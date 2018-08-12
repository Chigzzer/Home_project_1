import random

def dice_roll():
    numbers = range(1, 7)
    print("Resualt: {}".format(random.choice(numbers)))

dice_roll()