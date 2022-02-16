
class RetailItem:


    def __init__(self,desc,units,price):
        self.__Description = desc
        self.__Inventory = units
        self.__Price = price

    def get_item(self):
        return self.__Description

    def get_inv(self):
        return self.__Inventory

    def get_cost(self):
        return self.__Price

    def __str__(self):
        return 'The description is ' + self.__Description + ', the number of units is ' + format(self.__Inventory,',.0f') + ', and the price is $' + format(self.__Price,',.2f')