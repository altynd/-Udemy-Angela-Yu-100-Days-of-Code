from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello World!"

@app.route("/bye")
def say_bye():
    return "Bye"

if __name__ == "__main__":
    app.run(debug=True)

##Functions can have inputs/functionality/outputs
# def add(n1, n2):
#     return n1+n2
#
# def subtract(n1,n2):
#     return n1-n2
#
# def multiply(n1,n2):
#     return n1*n2
#
# def divide(n1,n2):
#     return n1/n2
#
# ##Functions are first class objects, can be passed around as arguments
# def calculate(calc_func, n1, n2):
#     return calc_func(n1,n2)
#
# result = calculate(add, 2,3)
# print(result)

## Functions can be nested in other functions
# def outer_function():
#     print("I am outer")
#
#     def nested_function():
#         print("I am inner")
#
#     nested_function()
#
# outer_function()

## Functions can be returned from other functions
# def outer_function():
#     print("I am outer")
#
#     def nested_function():
#         print("I am inner")
#
#     return nested_function
#
#
# inner_function = outer_function()
# inner_function()

##Python Decorator Function
# import time
#
# def delay_decorator(function):
#     def wrapper_function():
#         time.sleep(1)
#         function()
#         time.sleep(1)
#     return wrapper_function
#
# @delay_decorator
# def say_hello():
#     print("Hello")
#
# def say_bye():
#     print("Bye")
#
#
# say_hello()
# say_bye()

