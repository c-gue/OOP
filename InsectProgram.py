import InsectClass as i

def main():

    my_insect = i.Insect()


    print('The flight of this insect is: ', my_insect.get_flight())

    for count in range (10):
        my_insect.mile()
        distance = str(my_insect.mile())


    print("The insect flies: ", distance,'miles')

main()