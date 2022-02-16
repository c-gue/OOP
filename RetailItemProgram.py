import RetailItemClass as r


def main():


    item1 = r.RetailItem("Jacket",12,59.95)
    item2 = r.RetailItem("Designer Jeans",40,34.95)
    item3 = r.RetailItem("Shirt",20,24.95)

    print(item1.__str__())
    print(item2.__str__())
    print(item3.__str__())

    repeat = input("Would you like to revist any items? (y/n) ")

    while repeat == 'y':
        request = int(input("Which item number would you like to view? "))
        if request == 1:
            choice = input('Would you like to view the full item (all), description (d), units (u), or price (p)?')
            if choice == 'all':
                print(item1.__str__())
            elif choice == 'd':
                print(item1.get_item())
            elif choice == 'u':
                print(item1.get_inv())
            elif choice == 'p':
                print(item1.get_cost())
            else:
                print("Invalid input. Try again.") 
        elif request == 2:
            choice = input('Would you like to view the full item (all), description (d), units (u), or price (p)?')
            if choice == 'all':
                print(item2.__str__())
            elif choice == 'd':
                print(item2.get_item())
            elif choice == 'u':
                print(item2.get_inv())
            elif choice == 'p':
                print(item2.get_cost())
            else:
                print("Invalid input. Try again.") 
        elif request == 3:
            choice = input('Would you like to view the full item (all), description (d), units (u), or price (p)?')
            if choice == 'all':
                print(item3.__str__())
            elif choice == 'd':
                print(item3.get_item())
            elif choice == 'u':
                print(item3.get_inv())
            elif choice == 'p':
                print(item3.get_cost())
            else:
                print("Invalid input. Try again.") 
        else:
            print("Item not listed. Try again.")

        repeat = input("Would you like to revist any items? (y/n) ")

main()