from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        self.label_score = Label(text=f"Score {self.quiz.score}/{self.quiz.question_number}", fg="white", bg=THEME_COLOR)

        self.label_score.grid(column=2, row=1)

        self.canvas = Canvas(height=250, width=300, bg="white")
        self.quote_text = self.canvas.create_text(
            150,
            125,
            text="Some Question text",
            width=280,
            font=("Arial", 20, "italic"),
            fill=THEME_COLOR)
        self.canvas.grid(row=2, column=1, columnspan=2, pady=50)

        self.image_true = PhotoImage(file="images/true.png")
        self.button_true = Button(image=self.image_true,
                                  highlightcolor=THEME_COLOR,
                                  highlightthickness=0,
                                  highlightbackground=THEME_COLOR,
                                  command=self.true_pressed)
        self.button_true.grid(column=1, row=3)

        self.image_false = PhotoImage(file="images/false.png")
        self.button_false = Button(image=self.image_false,
                                   highlightcolor=THEME_COLOR,
                                   highlightthickness=0,
                                   highlightbackground=THEME_COLOR,
                                   command=self.false_pressed)
        self.button_false.grid(column=2, row=3)


        self.get_next_question()


        self.window.mainloop()


    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.quote_text, text=q_text)
        self.label_score.config(text=f"Score {self.quiz.score}/{self.quiz.question_number}")

    def true_pressed(self):
        if self.quiz.still_has_questions():
            self.quiz.check_answer("True")
            self.get_next_question()

    def false_pressed(self):
        if self.quiz.still_has_questions():
            self.quiz.check_answer("False")
            self.get_next_question()


