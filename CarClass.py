
class Car:

    def __init__(self,ym,make):
        self.__year_model = ym
        self.__make = make
        self.__speed = 0

    def accelerate(self):
        self.__speed += 5

    def brake(self):
        self.__speed -= 5

    def get_speed(self):
        return self.__speed

    def get_year_model(self):
        return self.__year_model
    
    def get_make(self):
        return self.__make