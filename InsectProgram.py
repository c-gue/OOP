import InsectClass as i

def main():

    my_insect = i.Insect()


    print('The flight of this insect is: ', my_insect.get_flight())

    for count in range (10):
        my_insect.flight()


    print("The insect flies: ", my_insect.get_flight())

main()