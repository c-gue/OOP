import RetailItemClass as r


def main():

    for i in range(3):
        item = int(input('What is your item number? '))
        desc = input('What item are you looking for? ')
        units = int(input('How many units are left in the inventory? '))
        price = float(input('How much does this item cost? '))
        
        if item == 1:
            item1 = ("Item #:",item,"Description:",desc,"Units:",units,"Price:",price)
            print(item1)
        elif item == 2:
            item2 = ("Item #:",item,"Description:",desc,"Units:",units,"Price:",price)
            print(item2)
        elif item == 3:
            item3 = ("Item #:",item,"Description:",desc,"Units:",units,"Price:",price)
            print(item3)

    repeat = input("Would you like to revist any items? (y/n) ")

    while repeat == 'y':
        request = int(input("Which item number would you like to view? "))
        if request == 1:
            print(item1)
        elif request == 2:
            print(item2)
        elif request == 3:
            print(item3)
        else:
            print("Item not listed. Try again.")

        repeat = input("Would you like to revist any items? (y/n) ")


main()