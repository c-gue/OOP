import random

class Insect:
    def __init__(self,w,l):
        self.wings = w
        self.leg = l
        self.flight = 0

    def flight_length(self):
        self.flight = random.randint(1,10)
        #return self.get_mile

    def get_miles(self):
        return self.flight