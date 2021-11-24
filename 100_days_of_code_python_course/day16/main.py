### Constructing Objects and Accessing their Attributes and Methods

# from turtle import Turtle, Screen
#
# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("yellow", "chartreuse4")
#
# my_screen = Screen()
#
# timmy.forward(100)
#
# my_screen.exitonclick()

### How to Add Python Packages and use PyPi
### Practice Modifying Object Attributes and Calling Methods

# from prettytable import PrettyTable
#
# table = PrettyTable()
#
# table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmaner"])
# table.add_column("Type", ["Electric", "Water", "Fire"])
#
# table.align = "l"
#
# print(table)

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_machine = CoffeeMaker()

menu = Menu()

payment_machine = MoneyMachine()

while True:
    options = menu.get_items()
    response = input(f'What would you like? ({options}): ')

    if response == 'off':
        break
    elif response == 'report':
        coffee_machine.report()
    else:
        item = menu.find_drink(response)
        if coffee_machine.is_resource_sufficient(item) and payment_machine.make_payment(item.cost):
            coffee_machine.make_coffee(item)
