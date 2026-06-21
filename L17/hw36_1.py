def my_decorator(funct):
    def wrapper():
        print("before")
        funct()
        print("after")
    return wrapper


@my_decorator
def say_hello():
    print("Hello")

#
# func = say_hello
# print(func)
# func()
say_hello()
# say_hello = my_decorator(say_hello)
# say_hello()