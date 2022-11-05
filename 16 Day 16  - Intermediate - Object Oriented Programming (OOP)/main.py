from menu import MENU



def report():
    print(
    "Water: 300 ml\n" 
    "Milk: 200ml\n" 
    "Coffee: 100g\n" 
    "Money: $0"
    )

while True:
    coffee_choose = input("What would you like? (espresso/latte/cappuccino): ")
    if coffee_choose == "report":
        report()
