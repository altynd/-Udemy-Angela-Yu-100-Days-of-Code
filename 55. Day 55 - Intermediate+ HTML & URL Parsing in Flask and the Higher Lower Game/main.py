from flask import Flask
from flask import render_template
import random

app = Flask(__name__)
app.app_context().push()  # for fast updates

answer_number = random.randint(1,9)
print(answer_number)

def make_bold(function):
    def inner():
        return f"<b>{function()}</b>"
    return inner

def make_emfes(function):
    def inner():
        return f"<em>{function()}</em>"
    return inner

def make_under(func):
    def inner():
        return f"<u>{func()}</u>"
    return inner

def decorate(func):
    def inner():
        return f"{func()}"
    return inner


@app.route("/bye")
@make_bold
@make_emfes
@make_under
def bye():
    return "Byu!"


@app.route("/")
def index():
    return "hello World"

@app.route("/<int:number>")
def guess(number):
    if number == answer_number:
        return render_template("/right.html")
    elif number>answer_number:
        return render_template("/high.html")
    else:
        return render_template("/low.html")


if __name__ == "__main__":
    app.run(debug=True)  # automatic starting app

