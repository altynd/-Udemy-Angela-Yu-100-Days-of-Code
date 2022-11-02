import random

print("Welcome to the PyPassword Generator")
letters = int(input("How many letters would you like in your password?"))
symbols = int(input("How many symbols would you like?"))
numbers = int(input("How many numbers would you like?"))

letters_data = ["a","b","c","d","e","f","g"]
symbols_data = ["!", "@", "#", "$", "%", "^"]

password=[]

for i in range(0,letters):
    letter_random = random.choice(letters_data)
    rand_cap = random.randint(0,1)
    if rand_cap == 1:
        letter_random = letter_random.title()
    password.append(letter_random)

for i in range(0,symbols):
    symbol_random = random.choice(symbols_data)
    password.append(symbol_random)

for i in range(0,numbers):
    number_random = random.randint(0,9)
    password.append(str(number_random))

random.shuffle(password)

pas_str=""
for i in password:
    pas_str = pas_str + i

print(pas_str)