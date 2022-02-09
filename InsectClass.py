import random

class Insect:
    def __init__(self):
        self.wings = 2
        self.leg = 4
        self.mile = 0

    def flight(self):
        if random.randint(1,10) == 1:
            self.mile = '1 Mile'
        elif random.randint(1,10)== 2:
            self.mile = '2 Miles'
        elif random.randint(1,10)== 3:
            self.mile = '3 Miles'
        elif random.randint(1,10)== 4:
            self.mile = '4 Miles'
        elif random.randint(1,10)== 5:
            self.mile = '5 Miles'
        elif random.randint(1,10)== 6:
            self.mile = '6 Miles'
        elif random.randint(1,10)== 7:
            self.mile = '7 Miles'
        elif random.randint(1,10)== 8:
            self.mile = '8 Miles'
        elif random.randint(1,10)== 9:
            self.mile = '9 Miles'
        else:
            self.mile = '10 Miles'



    def get_flight(self):
        return self.get_flight