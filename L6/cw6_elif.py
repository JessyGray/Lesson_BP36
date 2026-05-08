# b = 0
# if b == 0:
#     print(b)
#     b += 1
# elif b == 1:
#     print(b)
#     b += 1
# elif b == 2:
#     print(b)
#     b += 1
# else:
#     print("11111")

b = 0
if b < 10:
    print(b)
elif b < 15:
    print(b)
elif b < 20:
    print(b)
else:
    print("11111")

b = 0
if b < 10:
    print(b)
if b < 15:
    print(b)
if b < 20:
    print(b)
else:
    print("11111")


def divide_5(number):
    if number % 5 == 0:
        return "yes"
    return "no"


print(divide_5(25))
print(divide_5(23))


def divide_5(number):
    if number % 5 == 0:
        return "yes"
    return "no"


"""
False
0
""
[]
{}
set()
None

"""


def divide_5(number):
    if number % 5:
        return "no"
    return "yes"


# 10%3 = 1 10-10//3*3=1 9%3=0


def count_negative_numbers(x1, x2, x3):
    count = 0
    if x1 < 0:
        count += 1
    if x2 < 0:
        count += 1
    if x3 < 0:
        count += 1
    return count


print(count_negative_numbers(1, 1, 1))
print(count_negative_numbers(-1, 1, 1))
print(count_negative_numbers(1, -1, -1))
print(count_negative_numbers(-1, -1, -1))


print(True)
print(+True)
print(-True)
