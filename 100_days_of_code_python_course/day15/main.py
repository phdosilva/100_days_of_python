menu = {
    'espresso': {
        'ingredients': {
            'water': 50,
            'coffee': 18,
        },
        'cost': 1.5,
    },
    'latte': {
        'ingredients': {
            'water': 200,
            'milk': 150,
            'coffee': 24,
        },
        'cost': 2.5,
    },
    'cappuccino': {
        'ingredients': {
            'water': 250,
            'milk': 100,
            'coffee': 24,
        },
        'cost': 3.0,
    }
}

profit: float = 0

resources = {
    'water': 300,
    'milk': 200,
    'coffee': 100,
}


def report():
    print(f'water: {resources["water"]}ml' \
          f'\n' \
          f'milk: {resources["milk"]}ml' \
          f'\n' \
          f'coffee: {resources["coffee"]}ml' \
          f'\n' \
          f'profit. ${profit}')


def is_resource_sufficient(order_ingredients):
    """Return True when order can be made, False if ingredients are insufficient."""

    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f'Sorry there is not enough {item}.')
            return False
    return True


def process_coins():
    """Returns the total calculated from coins insert."""

    print('Please insert coins')
    total = int(input('how many quarters? ')) * 0.25
    total += int(input('how many dimes? ')) * 0.1
    total += int(input('how many nickles? ')) * 0.05
    total += int(input('how many pennies? ')) * 0.01

    return total


def is_money_sufficient(payment, order_price):
    """Return True when the payment is accepted and False when the payment is insufficient."""

    if payment >= order_price:
        return True
    print("Sorry that's not enough money. Money refunded.")
    return False


def calculate_profit(payment, order_prince):
    global profit
    profit += order_prince
    change = round(payment - menu['espresso']['cost'], 2)
    print(f'Here is ${change} in change.')

def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]

    print(f'Here is your {drink_name} ☕')

while True:
    response = input(f'What would you like? (espresso/latte/cappuccino): ')

    if response == 'off':
        break
    elif response == 'report':
        report()
    elif response == 'espresso':
        if is_resource_sufficient(menu['espresso']['ingredients']):
            payment = process_coins()
            if is_money_sufficient(payment, menu['espresso']['cost']):
                calculate_profit(payment, menu['espresso']['cost'])
                make_coffee('espresso', menu['espresso']['ingredients'])
    elif response == 'latte':
        if is_resource_sufficient(menu['latte']['ingredients']):
            payment = process_coins()
            if is_money_sufficient(payment, menu['latte']['cost']):
                calculate_profit(payment, menu['latte']['cost'])
                make_coffee('latte', menu['latte']['ingredients'])
    elif response == 'cappuccino':
        if is_resource_sufficient(menu['cappuccino']['ingredients']):
            payment = process_coins()
            if is_money_sufficient(payment, menu['cappuccino']['cost']):
                calculate_profit(payment, menu['cappuccino']['cost'])
                make_coffee('cappuccino', menu['cappuccino']['ingredients'])
