import CarClass as c

def main():

    car = c.Car('2003 Chevy','Silverado')
    print('Current Speed 0 is',car.get_speed(),'mph')
    for i in range(0,5):
        car.accelerate()
        print('Current Speed',i+1,'is',car.get_speed(),'mph')
    
    for i in range(5,10):
        car.brake()
        print('Current Speed',i+1,'is',car.get_speed(),'mph')

main()