from cw9.cw9_function import count_digit


def sum_digits(number: int) -> int:
    if type(number) is not int:
        print("please enter integer")
        return -1
    if number < 0:
        number = -number
    # if number == 0:
    #     return 0
    res = 0
    while number > 0:
        res += number % 10
        number //= 10
    return res


print(sum_digits(123))
print(sum_digits(-123))


def has_digit(number: int, digit: int) -> bool:
    if type(number) is not int or type(digit) is not int:
        print("please enter integer")
        return False
    if number < 0:
        number = -number
    if digit < 0:
        digit = -digit
    if digit > 9:
        return False
    if number==digit:
        return True
    while number!=0:
        if number%10==digit:
            return True
        number//=10
    return False

print(has_digit(12345,4))
print(has_digit(12345,6))
print(has_digit(4,4))
print(has_digit(-12345,4))
print(has_digit(12345,-6))
print(has_digit(4,-4))

# 123456 -> 23 True
#123456 ->32 False
#123456 -> 3456 True
def has_sub_number(number: int, sub_number: int) -> bool:
    if type(number) is not int or type(sub_number) is not int:
        print("please enter integer")
        return False
    if number < 0:
        number = -number
    if sub_number < 0:
        sub_number = -sub_number
    if sub_number>number:
        return False
    if number==sub_number:
        return True
    digits_sub_number = count_digit(sub_number)
    temp = 10**digits_sub_number
    while number>0:
        if number%temp==sub_number:
            return True
        number//=10
    return False


print(has_sub_number(12345678,123))
print(has_sub_number(12345678,1235))



