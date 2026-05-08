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

#match/case
def fan(mode: int) -> None:
    if type(mode) != int:
        print("Error: invalid type. Please enter integer")
        return
    match mode:
         case 1:
            print("Fan is running at speed 1.")
         case 2:
            print("Fan is running at speed 2.")
         case 3:
            print("Fan is running in turbo mode.")
         case 0:
            print("Fan is turned off.")
         case _:
            print("Error: invalid mode. Please enter 0, 1, 2, 3")


# fan(1)
# fan(2)
# fan(3)
# fan(0)
# fan(-1)
# fan(5)
# fan("hello")
# fan(True)


def calc(number1:float, number2:float, action:str)->tuple[float, str]:
# + - * / // % -> case "+"
    if type(number1) not in (float,int) or type(number2) not in (float,int) or type(action) is not str:
        return 0., "Error: invalid type"
    res = 0.
    match action:
        case '+':
            res = number1+number2
        case '-':
            res = number1 - number2
        case '*':
            res = number1 * number2
        case '//':
            if number2==0:
                res = None
            else:
                res = number1 // number2
        case '/':
            if number2==0:
                res = None
            else:
                res = number1 / number2
        case '%':
            if number2==0:
                res = None
            else:
                res = number1 % number2
        case _:
            res = None

    if res is None:
        return 0., "Error - operand or divide by zero"
    else:
        return res, ""


print(calc(12,6.,"+"))
print(calc(12,6.,"-"))
print(calc(12,6.,"*"))
print(calc(12,6,"/"))
print(calc(12,6,"//"))
print(calc(12,6,"%"))
print(calc(12,6,"9"))
print(calc(12,0,"/"))
print(calc(12,0,"//"))
print(calc(12,0,"%"))
print(calc("12",6,"/"))
print(calc(12,"6","//"))
print(calc(12,6,6))