def buy():
    option = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ')
    if order == 'back':
        return
    else:
        my_machine.check(option)

def fill():
    water_add = int(input('Write how many ml of water do you want to add: '))
    milk_add = int(input('Write how many ml of milk do you want to add: '))
    coffee_add = int(input('Write how many grams of coffee beans do you want to add: '))
    cups_add = int(input('Write how many disposable cups of coffee do you want to add: '))
    my_machine.fill(water_add, milk_add, coffee_add, cups_add)

def main():
    if order == 'buy':
        my_machine.main_action('buy')
    elif order == 'take':
        my_machine.main_action('take')
    elif order == 'fill':
        my_machine.main_action('fill')
    elif order == 'remaining':
        my_machine.main_action('remaining')

class CoffeeMachine:
    def __init__(self, water, milk, coffee, cups, money):
        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.cups = cups
        self.money = money

    def main_action(self, order):
        if order == 'fill':
             fill()
        elif order == 'take':
            self.take()
        elif order == 'remaining':
            self.remaining()
        elif order == 'buy':
            buy()
        else:
            pass

    def take(self):
        print(f'I gave you ${self.money}')
        self.money = 0

    def fill(self, water_add, milk_add, coffee_add, cups_add):
        self.water += water_add
        self.milk += milk_add
        self.coffee += coffee_add
        self.cups += cups_add

    def remaining(self):
        print(f'''The coffee machine has:
{self.water} of water
{self.milk} of milk
{self.coffee} of coffee beans
{self.cups} of disposable cups
${self.money} of money''')

    def check(self, option):
        if option == '1':
            if self.water < 250:
                print('Sorry, not enough water!')
            elif self.coffee < 16:
                print('Sorry, not enough coffee beans!')
            elif self.cups < 1:
                print('Sorry, not enough cups!')
            else:
                self.buy('espresso')
        elif option == '2':
            if self.water < 350:
                print('Sorry, not enough water!')
            elif self.milk < 75:
                print('Sorry, not enough milk!')
            elif self.coffee < 20:
                print('Sorry, not enough coffee beans!')
            elif self.cups < 1:
                print('Sorry, not enough cups!')
            else:
                self.buy('latte')
        elif option == '3':
            if self.water < 200:
                print('Sorry, not enough water!')
            elif self.milk < 100:
                print('Sorry, not enough milk!')
            elif self.coffee < 12:
                print('Sorry, not enough coffee beans!')
            elif self.cups < 1:
                print('Sorry, not enough cups!')
            else:
                self.buy('cappuccino')

    def buy(self, coffee_type):
        if coffee_type == 'espresso':
            self.water -= 250
            self.coffee -= 16
            self.money += 4
        elif coffee_type == 'latte':
            self.water -= 350
            self.milk -= 75
            self.coffee -= 20
            self.money += 7
        elif coffee_type == 'cappuccino':
            self.water -= 200
            self.milk -= 100
            self.coffee -= 12
            self.money += 6
        self.cups -= 1
        print('I have enough resources, making you a coffee!')

my_machine = CoffeeMachine(400, 540, 120, 9, 550)

while True:
    order = input('Write action (buy, fill, take, remaining, exit): ')
    if order == 'exit':
        break
    else:
        main()