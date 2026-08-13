from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

MENU = Menu()
coffee_ingredients = CoffeeMaker()
money = MoneyMachine()
turn_off = False

while not turn_off:
    user_order = input(f"What would you like to order? {MENU.get_items()}")
    if user_order.lower() == "report":
        coffee_ingredients.report()
        print(f"Profit: {money.CURRENCY}{money.profit}")
        continue

    if user_order.lower() == "off":
        turn_off = True
        break

    drink = MENU.find_drink(user_order)
    if drink:
        if coffee_ingredients.is_resource_sufficient(drink):

            if money.make_payment(drink.cost):
                coffee_ingredients.make_coffee(drink)