def fan(mode: int) -> None:
    if type(mode) != int:
        print("Error: invalid type. Please enter integer")
        return
    if mode == 1:
        print("Fan is running at speed 1.")
    elif mode == 2:
        print("Fan is running at speed 2.")
    elif mode == 3:
        print("Fan is running in turbo mode.")
    elif mode == 0:
        print("Fan is turned off.")
    else:
        print("Error: invalid mode. Please enter 0, 1, 2, 3")


fan(1)
fan(2)
fan(3)
fan(0)
fan(-1)
fan(5)
fan("hello")
fan(True)

def fan(mode: int) -> None:
    if not isinstance(mode,int) or isinstance(mode,bool):
        print("Error: invalid type. Please enter integer")
        return
    if mode == 1:
        print("Fan is running at speed 1.")
    elif mode == 2:
        print("Fan is running at speed 2.")
    elif mode == 3:
        print("Fan is running in turbo mode.")
    elif mode == 0:
        print("Fan is turned off.")
    else:
        print("Error: invalid mode. Please enter 0, 1, 2, 3")


fan(1)
fan(2)
fan(3)
fan(0)
fan(-1)
fan(5)
fan("hello")
fan(True)


def even_or_odd(number: int)->str:
    if type(number) is not int:
        return "Error: invalid type. Please enter integer"
    if number%2:
        return "The number is odd"
    return "The number is even"


print(even_or_odd(5))
print(even_or_odd(6))
print(even_or_odd("5"))


def my_age(age:int)->str:
    if type(age) is not int:
        return "Error: invalid type. Please enter integer"
    message = ""
    if age<0:
        message = "Error: Age cannot be negative."
    elif age<=18:
        message="Child"
    elif age<=67:
        message = "Adult"
    elif age <= 120:
        message = "Senior"
    else:
        message = "Error: Age cannot be > 120"
    return message


print(my_age(5))
print(my_age(0))
print(my_age(18))
print(my_age(19))
print(my_age(67))
print(my_age(68))
print(my_age(120))
print(my_age(125))
print(my_age(-5))
print(my_age("5"))
