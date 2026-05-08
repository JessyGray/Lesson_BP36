def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    return a / b


try:
    res = divide(10, 5)
    print(res)
except ValueError as error:
    print(error)

try:
    res = divide(10, 0)
    print(res)
except ValueError as my_error:
    print(my_error)


def calc(number1: float, number2: float, action: str) -> float:
    # + - * / // % -> case "+"
    if type(number1) not in (float, int):
        raise TypeError("number1 must be int or float")
    if type(number2) not in (float, int):
        raise TypeError("number2 must be int or float")
    if type(action) is not str:
        raise TypeError("action must be str")
    match action:
        case '+':
            return number1 + number2
        case '-':
            return number1 - number2
        case '*':
            return number1 * number2
        case '//':
            if number2 == 0:
                raise ZeroDivisionError("division by zero")
            return number1 // number2
        case '/':
            if number2 == 0:
                raise ZeroDivisionError("division by zero")
            return number1 / number2
        case '%':
            if number2 == 0:
                raise ZeroDivisionError("division by zero")
            return number1 % number2
        case _:
            raise ValueError("invalid action")


try:
    res = calc(10, 5, "/")
    print(res)
except TypeError as e:
    print(e)
except ZeroDivisionError as e:
    print(e)
except ValueError as e:
    print(e)

try:
    res = calc(10, 0, "/")
    print(res)
except TypeError as e:
    print(e)
except ZeroDivisionError as e:
    print(e)
except ValueError as e:
    print(e)

try:
    res = calc(10, "5", "/")
    print(res)
except TypeError as e:
    print(e)
except ZeroDivisionError as e:
    print(e)
except ValueError as e:
    print(e)

try:
    res = calc(10, 5, "---")
    print(res)
except TypeError as e:
    print(e)
except ZeroDivisionError as e:
    print(e)
except ValueError as e:
    print(e)
