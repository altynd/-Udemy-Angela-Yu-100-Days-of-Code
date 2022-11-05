print("Insert some coins")
quarters = int(input("How many quarters?"))*25/100
dimes = int(input("How many dimes?"))*10/100
nickels = int(input("How many nickels?"))*5/100
pennies = int(input("How many pennies?"))/100
money = quarters +dimes +nickels +pennies
print(money)
print(round(money))