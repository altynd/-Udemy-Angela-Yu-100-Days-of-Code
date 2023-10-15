def decorate(func):
    def inner():
        return f"{func()}"
    return inner



@decorate
def hi():
    print("Say Hi")

@decorate
def bye():
    print("say Bye")

hi()