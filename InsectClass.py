import random

class Insect:
    def __init__(self):
        self.wings = 2
        self.leg = 4
        self.flight = 0

    def flight_length(self):
        self.flight = random.randint(1,10)
        #return self.get_mile

    def get_miles(self):
        return self.flight