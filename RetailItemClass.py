from operator import itemgetter
from pydoc import describe
from tkinter import UNITS


class RetailItem:


    def __init__(self,item,desc,units,price):
        self.__ItemNumber = item
        self.__Description = desc
        self.__Inventory = units
        self.__Price = price


    def number(self,itemno):
        self.number = itemno
    
    def item(self,description):
        self.item = description

    def inv(self,count):
        self.inv = count

    def cost(self,rp):
        self.cost = rp

    def get_number(self):
        return self.__ItemNumber

    def get_item(self):
        return self.__Description

    def get_inv(self):
        return self.__Inventory

    def get_cost(self):
        return self.__Price