import tkinter
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Courier"
current_card=None
to_learn=None

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    to_learn=data.to_dict("records")
else:
    to_learn = data.to_dict("records")

def object_config(object):
    return object.config(background=BACKGROUND_COLOR,
                         highlightcolor=BACKGROUND_COLOR,
                         highlightthickness=0,
                         highlightbackground=BACKGROUND_COLOR)


def next_card():
    global current_card
    global flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(image_card, image=image_card_front)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    global current_card
    canvas.itemconfig(card_title, text = "English", fill='white')
    canvas.itemconfig(card_word, text=current_card["English"], fill='white')
    canvas.itemconfig(image_card, image=image_card_back)

def is_known():
    """remove card from the wor list to_learn"""
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv",index=False)
    print(len(to_learn))
    next_card()

def is_unknown():
    """do something"""
    next_card()

window = tkinter.Tk()
window.title("Flashy")
window.minsize(width=900, height=750)
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)


canvas = tkinter.Canvas(width=800, height=526)
image_card_back = tkinter.PhotoImage(file="images/card_back.png")
image_card_front = tkinter.PhotoImage(file="images/card_front.png")
image_card = canvas.create_image(400, 263, image=image_card_front)

card_title = canvas.create_text(400, 100, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 300, text="", font=("Ariel", 50, "bold"))
object_config(canvas)
canvas.grid(column=1, row=1, columnspan=2)

image_right = tkinter.PhotoImage(file="images/right.png")
button_known = tkinter.Button(image=image_right, command=is_known)
object_config(button_known)
button_known.grid(column=1, row=2)

image_wrong = tkinter.PhotoImage(file="images/wrong.png")
button_unknown = tkinter.Button(image=image_wrong, command=is_unknown)
object_config(button_unknown)
button_unknown.grid(column=2, row=2)

flip_timer = window.after(3000, func=flip_card)

next_card()

window.mainloop()
