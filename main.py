from car import Car

if __name__ == '__main__':
    n = int(input('Enter a value: '))

    cars = []
    for i in range(n):
        model = input("Enter a model: ")
        year = input('Enter year: ')
        price = input('Enter a price: ')

        car = Car(model, year, price)
        cars.append(car)

    for car in cars:
        car.display_info()
        car.start()

