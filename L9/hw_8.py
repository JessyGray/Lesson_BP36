# Task1
# def positive_integer(number: int) -> int:
#     if type(number) is not int:
#         print("Invalid type error")
#         return -1
#     if number < 0:
#         print("Error: Please enter positive number")
#         return -1
#     res = 0
#     reverse = 0
#     while number > 0:
#         res = number % 10
#         reverse = reverse * 10 + res
#         number //= 10
#
#     while reverse > 0:
#         res= reverse%10
#         reverse//=10
#         print(res)
# positive_integer(45326)
# Task2
def is_prime_number(number: int) -> bool:
    if type (number)  is not int:
        return (False,"Error: Invalid type")
    div=2
    while div < number:
        number%div
        div=+1

    return False



print(is_prime_number(3))