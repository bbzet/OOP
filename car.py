class Car:
    def __init__(self, model=None, year=None, price=None, made='Japan'):
        self.made = made
        self.model = model
        self.year = year
        self.price = price
        self.started = False


    def display_info(self):
        print(f'Make: {self.made}')
        print(f'Model: {self.model}')
        print(f'Year: {self.year}')
        print(f'Price: {self.price}')


    def start(self):
        if not self.started:
            print(f'{self.model} get started')
            self.started = True
        else:
            print(f'{self.model} is already started')


    def off_machine(self):
        if self.started:
            print(f'{self.model} turned off')
            self.started = False
        else:
            print(f'{self.model} is already turned off')

