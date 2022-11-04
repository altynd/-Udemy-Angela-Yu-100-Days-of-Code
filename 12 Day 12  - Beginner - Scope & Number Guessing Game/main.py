import random

random_number = random.randint(1,100)

print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100")
difficulty = input("Choose a difficalty. Type 'easy' or 'hard'")

if difficulty == "hard":
    remaining = 5
    print(f"You have {remaining} attempts to guess the  number")
else:
    remaining = 10
    print(f"You have {remaining} attempts to guess the  number")

print(f"random number {random_number}")

def guess_again():
    global remaining
    global game_continig
    print("Guess again")
    remaining -= 1
    if remaining >0:
        print(f"You have {remaining} attemps to guess the  number")
    else:
        print("You have run out of guesses, you lose")
        game_continig = False

def calculate():
    global game_continig
    if guess == random_number:
        print("You win!")
        game_continig = False
        return
    elif guess > random_number:
        print("Too high")
    elif guess < random_number:
        print("Too low")
    guess_again()


game_continig = True
while game_continig:
    guess = int(input("Make a guess:"))
    calculate()





