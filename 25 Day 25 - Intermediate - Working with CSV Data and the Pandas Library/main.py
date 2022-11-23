# # # with open("weather_data.csv") as file:
# # #     data = file.readlines()
# # # print(data)
# #
# # # import csv
# # # with open("weather_data.csv") as file:
# # #     data = csv.reader(file)
# # #     temperatures = []
# # #     for row in data:
# # #         if row[1] != "temp":
# # #             temperatures.append(row[1])
# # # print(temperatures)
# #
# # import pandas
# # data = pandas.read_csv("weather_data.csv")
# # # print(data)
# #
# # #average
# # # temp_list = data["temp"].to_list()
# # # print(temp_list)
# # # temp_average = sum(temp_list)/len(temp_list)
# #
# # # temp_average = data["temp"].mean()
# # # print(temp_average)
# # #
# # # temp_max = data.temp.max()
# # # print(temp_max)
# #
# # #Row
# # # print(data[data.day == "Monday"])
# #
# #
# # # print(data[data.temp == data.temp.max()])
# # # print(data[data.day == "Monday"])
# #
# # #Create data
# # data_dict = {
# #     "students":["Amy", "James", "Angela"],
# #     "scores": [76, 56, 65]
# # }
# # data = pandas.DataFrame(data_dict)
# # data.to_csv("new_data.csv")
#
# import pandas
#
# gray = 0
# cinnamon = 0
# black = 0
#
# data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# # colors = data["Primary Fur Color"]
# # for color in colors:
# #     if color == "Gray":
# #         grey+=1
# #     elif color == "Cinnamon":
# #         cinnamon += 1
# #     elif color == "Black":
# #         black +=1
# grey = data[data["Primary Fur Color"] == "Gray"]
# grey_count = len(grey)
# cinnamon = data[data["Primary Fur Color"] == "Cinnamon"]
# cinnamon_count = len(cinnamon)
# black = data[data["Primary Fur Color"] == "Black"]
# black_count = len(black)
#
# new_data = {
#     "Color": ["grey", "cinnamon", "black"],
#     "count": [grey_count, cinnamon_count, black_count],
# }
#
# df = pandas.DataFrame(new_data)
# df.to_csv("new_data.csv")

import turtle

import pandas

screen = turtle.Screen()
screen.title("US States")
img = "blank_states_img.gif"

screen.addshape(img)
turtle.shape(img)
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
points = turtle.Turtle()

chanses = len(all_states)
guessed_states = []
guessed_state = len(guessed_states)

points.penup()
points.hideturtle()
points.goto(150, 150)
points.write(f"{guessed_state} / {chanses}", font=('Arial', 25))


while len(guessed_states) < chanses:
    answer_state = screen.textinput(title="Guess the State", prompt="Whats the state name").title()

    if answer_state in all_states:
        state_data = data[answer_state == data.state]
        town = turtle.Turtle()
        town.penup()
        town.hideturtle()
        town.goto(int(state_data.x), int(state_data.y))
        # town.write(state_data.state.item())
        guessed_states.append(answer_state)
        town.write(answer_state)
        guessed_state = guessed_state + 1
        points.clear()
        points.write(f"{guessed_state} / {chanses}", font=('Arial', 25))
    elif answer_state == "Exit":
        break
    else:
        print("Wrong")
    print(guessed_state)

states_to_learn = []

for state in all_states:
    if state not in guessed_states:
        states_to_learn.append(state)

df = pandas.DataFrame(states_to_learn)
df.to_csv("states_to_learn.csv")

# turtle.mainloop()
# screen.exitonclick()
