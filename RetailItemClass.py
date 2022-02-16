
class RetailItem:


    def __init__(self,item,desc,units,price):
        self.__ItemNumber = item
        self.__Description = desc
        self.__Inventory = units
        self.__Price = price

    def get_number(self):
        return self.__ItemNumber

    def get_item(self):
        return self.__Description

    def get_inv(self):
        return self.__Inventory

    def get_cost(self):
        return self.__Price

    def __str__(self):
        #return 'The item # is ' + self.__ItemNumber + ', the description is ' + self.__Description + ', the units in inventory is' + self.__Inventory + ', and the price is $' + self.__Price
        return 'The item # is ' + format(self.__ItemNumber,',.0f') + ', the description is ' + self.__Description + ', the number of units is ' + format(self.__Inventory,',.0f') + ', and the price is $' + format(self.__Price,',.2f')