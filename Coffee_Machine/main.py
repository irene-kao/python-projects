# This program simulates a coffee machine by asking for your order, making your drink, and dispensing change

from menu import MENU


def coffee_machine():
    resources = {"water": 300, "milk": 200, "coffee": 100, "money": 0}

    def report():
        for values in resources:
            print(f"{values}: {resources[values]}")

    def check_resources(drink):
        enough = True
        if drink == "espresso" or drink == "latte" or drink == "cappuccino":
            check_me = MENU[drink]["ingredients"]
            for ingredient in check_me:
                if resources[ingredient] < check_me[ingredient]:
                    enough = False
                    print(f"Sorry, there is not enough {ingredient}.")
            if not enough:
                print("A barista will refill me now.")
                return False
            else:
                return True
        else:
            print("Invalid input. Try again.")
            machine_is_on()

    def process_coins():
        print("Insert coins. Espresso: $1.5, Latte: $2.5, Cappuccino: $3.0")
        # An alternative way is to keep running total after each input
        pennies = float(input("Pennies: "))
        nickels = float(input("Nickels: "))
        dimes = float(input("Dimes: "))
        quarters = float(input("Quarters: "))
        total_amount = (pennies*0.01) + (nickels*0.05) + (dimes*0.1) + (quarters*0.25)
        return total_amount

    def coin_transaction(amount, drink):
        cost = MENU[drink]["cost"]
        if cost > amount:
            cost = round(cost, 2)
            print(f"Sorry, that's not enough money - {drink}s cost ${cost}. Money refunded.")
            return False
        else:
            resources["money"] += cost
            if cost < amount:
                change = round(amount - cost, 2)
                print(f"Your change is ${change}.")
                return True
            return True

    def make_coffee(drink):
        drink_ingredients = MENU[drink]["ingredients"]
        for item in drink_ingredients:
            resources[item] -= drink_ingredients[item]
        print(f"Here is your {drink}, enjoy!")

    def machine_is_on():
        on = True
        while on:
            drink_choice = input("\nWhat would you like - espresso, latte, or cappuccino? "
                                 "\nYou can also print 'report'")
            if drink_choice == "report":
                report()
                machine_is_on()
            if check_resources(drink_choice):
                user_paid = process_coins()
                if coin_transaction(user_paid, drink_choice):
                    make_coffee(drink_choice)
                else:
                    machine_is_on()
            else:
                coffee_machine()

    power_switch = input("\nDo you want to turn the coffee machine on or off? ").lower()
    if power_switch == "off":
        exit()
    else:
        machine_is_on()


coffee_machine()
