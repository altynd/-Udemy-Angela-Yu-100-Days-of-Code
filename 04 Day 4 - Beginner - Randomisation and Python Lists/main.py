import random

my_choose = int(input("What do you choose? Type  0 for Rock, 1 for Paper or 2 for Scissors"))

computer_choose = random.randint(0,2)

def choose(i):
    if i == 0:
        return "choose Rock"
    elif i ==1:
        return "choose Paper"
    else:
        return "choose Scissors"

def game():
    print(f"your {choose(my_choose)}")
    print(f"computer {choose(computer_choose)}")

    if my_choose == 0 and computer_choose == 2:
        print("WIN")
    elif my_choose == computer_choose:
        print("Ni4ya!")
    elif my_choose > computer_choose:
        print("WIN")
    else:
        print("LOSE")

game()


