def count_divisible_three(number: int) -> int:
    if type(number) is not int:
        print("please enter integer")
        return -1
    if number < 0:
        print("please enter positive number")
        return -1
    if number == 0:
        return 1
    count = 0
    while number > 0:
        if not number % 10 % 3:
            """
            n = number%10
            temp = n%3
            temp==0
            """
            count += 1
        number //= 10
    return count


print(count_divisible_three(123456789))
print(count_divisible_three(1230))
print(count_divisible_three(0))
print(count_divisible_three(-123456789))
print(count_divisible_three("-123456789"))


def lcm(a: int, b: int) -> int:
    if type(a) is not int or type(b) is not int:
        print("please enter integer")
        return -1
    if a < 0 or b < 0:
        print("please enter positive number")
        return -1
    if a == 0 or b == 0:
        return min(a, b)
    res = max(a, b)
    step_ = res
    while res <= a * b:
        if res % a == 0 and res % b == 0:
            return res
        res += step_

    return -1


print(lcm(2, 6))
print(lcm(2, 7))
print(lcm(2, 5))
print(lcm(2, 0))
print(lcm("2", 6))
print(lcm(2, -6))


def print_stars(stars: int) -> None:
    if type(stars) is not int:
        print("please enter integer")
        return
    if stars <= 0:
        print("please enter positive number")
        return
    print("*" * stars)


print_stars(10)


def print_stars_adv(stars: int, column: int) -> None:
    if type(stars) is not int or type(column) is not int:
        print("please enter integer")
        return
    if stars <= 0 or column <= 0:
        print("please enter positive number")
        return
    while stars > column:
        print("*" * column)
        stars -= column
    print("*" * stars)


print_stars_adv(18, 5)


def factorial(number: int) -> int:
    if type(number) is not int:
        print("please enter integer")
        return -1
    if number < 0:
        print("please enter positive number")
        return -1
    if number == 0:
        return 1
    res = 1
    while number > 0:
        res *= number
        number -= 1
    return res


print(factorial(5))
print(factorial(0))


def factorial_rec(number: int) -> int:
    if type(number) is not int:
        print("please enter integer")
        return -1
    if number < 0:
        print("please enter positive number")
        return -1
    if number == 0 or number == 1:
        return 1
    return number * factorial_rec(number - 1)

"""
number = 5
factorial_rec(5)
return 5* factorial_rec(4)
factorial_rec(4)
return 4* factorial_rec(3)
factorial_rec(3)
return 3* factorial_rec(2)
factorial_rec(2)
return 2* factorial_rec(1)
factorial_rec(1)
return 1 
126-> 1*2
124->3*2*1
122->4*3*2*1
120-> 5*4*3*2*1
"""