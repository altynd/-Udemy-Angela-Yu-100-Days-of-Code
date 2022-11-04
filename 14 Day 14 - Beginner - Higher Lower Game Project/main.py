from data import data
import random

work_data = data
points = 0

print("Higher lower game")


def choose_data():
    global work_data
    global game_continue
    """Pick random item in dict data and removes it  from dict"""
    dict = random.choice(work_data)
    work_data.remove(dict)
    return dict


def print_result(dict, index):
    """Prin question from data dict"""
    print(f"Compare {index}: {dict['name']}, {dict['description']}, from {dict['country']}")


def compare(what_chhose):
    global dict_a
    global dict_b
    global points
    global game_continue
    if what_chhose == "A":
        if dict_a["follower_count"] > dict_b["follower_count"]:
            points += 1
            print(f"You are right!, You have a {points} points")
        else:
            print(f"You are  wrong, Game Over. You have a {points} points")
            game_continue = False
    else:
        if dict_a["follower_count"] < dict_b["follower_count"]:
            points += 1
            print(f"You are right!, You have a {points} points")
        else:
            print(f"You are  wrong, Game Over. You have a {points} points")
            game_continue = False
    dict_a = dict_b
    dict_b = choose_data()


dict_a = choose_data()
dict_b = choose_data()
game_continue = True
while game_continue:
    print("_______NEW GAME___________")
    print_result(dict_a, "A")
    print(f"VS")
    print_result(dict_b, "B")

    answer = input("Who has more followers? Type 'A' or 'B':")

    if answer == "A" or answer == "a":
        compare("A")

    elif answer == "B" or answer == "b":
        compare("B")
