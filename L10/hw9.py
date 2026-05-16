def count_digits(number: int) -> int:
    if type(number) is not int:
        print("Error: number must be an integer.")
        return -1
    if number < 0:
        number = -number
    if number == 0:
        return 1
    count = 0
    while number > 0:
        count += 1
        number //= 10
    return count


def print_digits(number:int)->None:
    if type(number) is not int:
        print("Error type")
        return
    if number<0:
        print("error - only positive number")
        return
    digits_count = count_digits(number)
    divisor = 10**(digits_count-1)
    while divisor>0:
        digit=number//divisor
        print(digit)
        number%=divisor
        divisor//=10
"""
number = 112
digits_count=3
divisor = 100
1 iteration ->100>0 => digit = 1 (1) number=12 divisor = 10
2 iteration ->10>0 => digit = 1 (1) number=2 divisor = 1
3 iteration ->1>0 => digit = 2 (2) number=0 divisor = 0

"""

print_digits(112)
print_digits(11200)
print_digits(10012)


def is_prime_number(number:int)->bool:
    if type(number) is not int:
        print("Error type")
        return False
    if number<=1:
        return False
    if number ==2:
        return True
    if number%2==0:
        return False
    divisor = 3
    while divisor*divisor<=number:
        if number%divisor==0:
            return False
        divisor+=2
    return True


print(is_prime_number(113))
print(is_prime_number(114))
print(is_prime_number(2027))
print(is_prime_number(2026))

#112233
def is_lucky_number(number:int)->bool:
    if type(number) is not int:
        print("Error type")
        return False
    if number < 10:
        return False
    total_sum = 0
    while number>0:
        total_sum+=number%10
        number//=10
        total_sum-=number%10
        number//=10
    return total_sum==0

# 1122 => total_sum=2 112 total_sum=2-2=0 11
#11 total_sum=1 12 total_sum=1-1 0
#1
print(is_lucky_number(1122))
print(is_lucky_number(12345))

