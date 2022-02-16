import RetailItemClass as r


def main():

    itemno1 = int(input('What is your item number? '))
    description1 = input('What item are you looking for? ')
    count1 = int(input('How many units are left in the inventory? '))
    rp1 = float(input('How much does this item cost? '))

    itemno2 = int(input('What is your item number? '))
    description2 = input('What item are you looking for? ')
    count2 = int(input('How many units are left in the inventory? '))
    rp2 = float(input('How much does this item cost? '))

    itemno3 = int(input('What is your item number? '))
    description3 = input('What item are you looking for? ')
    count3 = int(input('How many units are left in the inventory? '))
    rp3 = float(input('How much does this item cost? '))

    item1 = r.RetailItem(itemno1,description1,count1,rp1)
    item2 = r.RetailItem(itemno2,description2,count2,rp2)
    item3 = r.RetailItem(itemno3,description3,count3,rp3)

    print(item1.__str__())
    print(item2.__str__())
    print(item3.__str__())

    repeat = input("Would you like to revist any items? (y/n) ")

    while repeat == 'y':
        request = int(input("Which item number would you like to view? "))
        if request == 1:
            print(item1.__str__())
        elif request == 2:
            print(item2.__str__())
        elif request == 3:
            print(item3.__str__())
        else:
            print("Item not listed. Try again.")

        repeat = input("Would you like to revist any items? (y/n) ")


main()