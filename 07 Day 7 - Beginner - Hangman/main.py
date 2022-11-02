import random

word_list = ["ardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

display = []
for letter in chosen_word:
    display.append("_")

lives = 6
end_of_game = False
while not end_of_game:
    guess = input("Guess the letter").lower()
    for position in range(len(chosen_word)):
        if chosen_word[position] == guess:
            display[position] = guess

    print(display)

    if guess not in chosen_word:
        lives -=1
        if lives == 0:
            end_of_game=True
            print("You Lose!")

    if "_" not in display:
        end_of_game = True
        print("You Win!")












