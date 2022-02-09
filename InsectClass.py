import random

class Insect:
    def __init__(self):
        self.wings = 2
        self.leg = 4
        self.mile = 0

    def flight(self):
        self.get_mile = random.randint(1,10)
        return self.get_mile