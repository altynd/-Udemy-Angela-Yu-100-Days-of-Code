import tkinter

#-----------------CONSTANTS-----------------
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 1
CHECKMARK = "✔"
timer = None


#-----------------UI SETUP-----------------
window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW, highlightthickness=0, highlightcolor=YELLOW, highlightbackground=YELLOW)
window.minsize(width=200, height=224)

canvas = tkinter.Canvas(width=200, height=224)
canvas.config(bg=YELLOW)
image = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(102,112,image=image)
timer_text = canvas.create_text(103,130, text="00:00", fill="white", font=(FONT_NAME,35,"bold"))
canvas.grid(row=2, column=2)

label_text_timer = tkinter.Label(text="TIMER", font=(FONT_NAME, 50, "bold",))
label_text_timer.config(fg=GREEN, bg=YELLOW)
label_text_timer.grid(row=1, column=2)
label_checkmark = tkinter.Label(text="", fg=GREEN, bg=YELLOW)
label_checkmark.grid(row=4, column=2)

def start_timer():
    global reps
    global CHECKMARK
    # while reps<7:

    if reps == 8:
        count_down(LONG_BREAK_MIN*60)
        label_text_timer.config(text="BREAK", fg=RED)
    elif reps % 2 == 1 :
        count_down(WORK_MIN*60)
        label_text_timer.config(text="WORK", fg=GREEN)
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN*60)
        label_text_timer.config(text="BREAK", fg=PINK)
        label_checkmark.config(text=CHECKMARK)
        CHECKMARK+="✔"

    reps+=1
    if reps == 9:
        reps = 1

def reset_timer():
    global reps
    global CHECKMARK
    global timer
    reps=1
    CHECKMARK= ""
    label_text_timer.config(text="TIMER", fg=GREEN)
    canvas.itemconfig(timer_text, text = "00:00")
    #stop timer
    window.after_cancel(timer)


button_start = tkinter.Button(text="Start", bg=YELLOW, highlightthickness=0, highlightcolor=YELLOW, highlightbackground=YELLOW, command=start_timer)
button_start.grid(row=3, column=1)
button_reset = tkinter.Button(text="Reset", bg=YELLOW, highlightthickness=0, highlightcolor=YELLOW, highlightbackground=YELLOW, command=reset_timer)
button_reset.grid(row=3, column=3)

#-----------------COUNTDOWN MECHANISM-----------------

def count_down(count_sec):
    global reps
    global timer
    minutes = count_sec // 60
    seconds = count_sec % 60
    if minutes < 10:
        minutes = f"0{minutes}"
    if seconds < 10:
        seconds = f"0{seconds}"
    display_time = f"{minutes}:{seconds}"

    canvas.itemconfig(timer_text, text=display_time)
    if count_sec >0:
        timer = window.after(1000, count_down, count_sec - 1)
    else:
        start_timer()



window.mainloop()
