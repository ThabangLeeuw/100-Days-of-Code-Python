# TODO 2: Import the necessary data from the MENU module
from MENU import MENU, resources


def options(user_option):
    return MENU[user_option]

def report():
    for i in resources:
        print(f"{i}: {resources[i]}")
    return resources

def enoughResources(user_option):
    # Check if all ingredients are available
    for i in MENU[user_option]["ingredients"]:
        if MENU[user_option]["ingredients"][i] > resources[i]:
            return f"Sorry, not enough {i} to make a {user_option}, here is your refund."
    return True


turn_off = True

# TODO 1: Prompt user by asking what they would like to order.

while turn_off:
    quater, dimes, nickles, pennies = 0.25, 0.10, 0.05, 0.01
    total = 0
    user_option = input("What  would you like? (espresso/latte/cappuccino): ")
    if user_option == "report".lower():
        report()
    elif (user_option == "espresso".lower()) or (user_option == "latte".lower()) or (user_option == "cappuccino".lower()):
        quaters = int(input("How many quaters?: ")) * quater
        dimess = int(input("How many dimes?: ")) * dimes
        nickless = int(input("How many nickles?: ")) * nickles
        penniess = int(input("How many pennies?: ")) * pennies
        total = quaters + dimess + nickless + penniess
        if total >= MENU[user_option]["cost"]:
            check = enoughResources(user_option)
            if check == True:
                # Deduct resources only after payment succeeds
                for i in MENU[user_option]["ingredients"]:
                    resources[i] -= MENU[user_option]["ingredients"][i]
                change = total - MENU[user_option]["cost"]
                print(f"Here is your change ${change:.2f}\nEnjoy your {user_option}! ☕")
                resources["money"] += MENU[user_option]["cost"]
            else:
                print(check)  # prints the refund message
        else:
            print(f"Sorry, ${total:.2f} is not enough to make a {user_option}. Here is your refund.")

    switch_off = input("Do you wish to switch the machine off? Type 'off': ")
    if switch_off.lower() == "off".lower():
        turn_off = False



