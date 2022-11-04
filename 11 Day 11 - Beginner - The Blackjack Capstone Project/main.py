import random
import time

all_cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

user_cards = []
dealer_cards = []
money = 100
game_continue = True


def take_card_into_koloda(cards):
    card = random.choice(all_cards)
    cards.append(card)
    if cards == user_cards:
        print(f"On your hands {cards}")
    else:
        print(f"On dealer hands {cards}")
    time.sleep(1)
    return card


def win():
    global money
    global game_continue
    time.sleep(1)
    print("You win")
    money = money + 1
    print(f"You have {money} money")
    time.sleep(1)
    game_continue = False


def lose():
    global money
    global game_continue
    time.sleep(1)
    print("You lose")
    money = money - 1
    print(f"You have {money} money")
    time.sleep(1)
    game_continue = False


def draw():
    global game_continue
    time.sleep(1)
    print("It is Draw!")
    print(f"You have {money} money")
    time.sleep(1)
    game_continue = False


def calculate(cards):
    user_points = sum(user_cards)
    dealer_points = sum(dealer_cards)
    global money
    global game_continue

    if cards == user_cards:
        print(f"You have {user_points} points")
        if user_points == 21:
            print("You take Black Jack!")
            win()
        elif user_points > 21:
            lose()

    elif cards == dealer_cards:
        print(f"Dialer have {dealer_points} points")
        if dealer_points == 21:
            print("Dealer take Black Jack!")
            lose()
        elif dealer_points <= 17 or dealer_points < user_points:
            take_card_into_koloda(dealer_cards)
            calculate(dealer_cards)
        elif dealer_points == user_points:
            draw()
        elif dealer_points > 21:
            win()
        elif dealer_points < user_points:
            win()
        else:
            lose()


def def_game_continue():
    global game_continue
    while game_continue:
        game_answer = input("Would you like take another card?")
        if game_answer == "y":
            take_card_into_koloda(user_cards)
            calculate(user_cards)
        else:
            take_card_into_koloda(dealer_cards)
            calculate(dealer_cards)


def game_restart():
    global game_continue
    global user_cards
    global dealer_cards

    if input("Want to play? print y: ") == "y":
        game_continue = True
        user_cards = []
        dealer_cards = []
        print("-------Game starts---------")
        game_start()
    else:
        time.sleep(1)
        print("Good bye!")


def game_start():
    # take card
    take_card_into_koloda(user_cards)
    take_card_into_koloda(user_cards)
    take_card_into_koloda(dealer_cards)

    calculate(user_cards)

    def_game_continue()

    game_restart()


if __name__ == '__main__':
    game_start()
