#ALL WORKING
#Change coins

from menu import MENU
from menu import resources

coffee_price = None
menu = MENU

#TODO-3
def report():
    """prints resourses """
    for key in resources:
        print(f"{key} : {resources[key]}")


def making(coffee_chosen):
    for menu_item in menu:
        if menu_item == coffee_chosen:
            #TODO-4
            coffee_ingredients = menu[coffee_chosen]["ingredients"]
            for ingredient in coffee_ingredients:
                if resources[ingredient] > coffee_ingredients[ingredient]:
                    enouth_resources = True
                else:
                    print(f"Sorry, Not anouth {ingredient}")
                    return
            #TODO-5
            coffee_price = menu[coffee_chosen]["cost"]
            money = coins()
            #TODO-6
            if money > coffee_price and enouth_resources:
                resources["money"] = resources["money"] + coffee_price
                change = round((money - coffee_price),2)

                print(f"Here is ${change} in change")
                #TODO-7
                for ingredient in coffee_ingredients:
                    resources[ingredient] = resources[ingredient] - coffee_ingredients[ingredient]
                print(f"Here is your {coffee_chosen}, Enjoy!")
            else:
                print("Not enough money")
                print(f"Here is your money: {money}")
                print(f"Insert more coins {coffee_price}")

#TODO-5
def coins():
    print("Insert some coins")
    quarters = int(input("How many quarters?"))*25/100
    dimes = int(input("How many dimes?"))*10/100
    nickels = int(input("How many nickels?"))*5/100
    pennies = int(input("How many pennies?"))/100
    money = quarters +dimes +nickels +pennies
    return money

is_working = True
while is_working:
    #TODO-1
    coffee_choosen = input("What would you like? (espresso/latte/cappuccino): ")
    #TODO-2
    if coffee_choosen == "off":
        is_working = False
        print("Coffe mashine OFF")
    #TODO-3
    elif coffee_choosen == "report":
        report()
    #TODO-4 TODO-5 TODO-6 TODO-7
    else:
        making(coffee_choosen)





