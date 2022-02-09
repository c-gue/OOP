import CellPhoneClass as cp

apple = cp.CellPhone("Apple","H4395",950.99)

def main():

    print("The manufacturer is ",apple.get_manufact())
    print("The model is ",apple.get_model())
    print("The retail price is ", apple.get_retail_price())

main()