

# from my_module import pi
# print(pi)

# import random
# test_seed = int(input("Create a seed number:"))
# random.seed(test_seed)
#
# random_number = random.randint(0,1)
# if random_number == 0:
#     print("Tails")
# else:
#     print("Seed")


# import random
# # states_of_america = ["Delawere", "Pensilvania", "New Jersy", "Georgia"]
#
# names = input("Give me a names")
# names_list = names.split(", ")
# print(names_list)
# random_name = random.choice(names_list)
# print(random_name)


# row1 = ["🌝", "🌝", "🌝"]
# row2 = ["🌝", "🌝", "🌝"]
# row3 = ["🌝", "🌝", "🌝"]
# map = [row1,row2,row3]
# print(f"{row1}\n{row2}\n{row3}")
#
# position = input("Where you want to put the treasure?")
# x = int(position[0])-1
# y = int(position[1])-1
#
# map[y][x]="🌚"
# print(f"{row1}\n{row2}\n{row3}")


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