print("Welcome to the Number Guessing Game!")
print("i am thinking of a number between 1 and 100")
difficulty = input("Choose a difficalty. Type 'easy' or 'hard'")

if difficulty == "hard":
    remaining = 5
else:
    remaining = 10

print(f"You have {remaining} attemps to guess the  number")
guess = input("Make a guess:")