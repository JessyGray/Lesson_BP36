# Task1
def positive_integer(number: int) -> int:
    if type(number) is not int:
        print("Invalid type error")
        return -1
    if number <= 0:
        print("Error: Please enter positive number")
        return -1

    res = 0
    reverse = 0
    while number > 0:
        res = number % 10
        reverse = reverse * 10 + res
        number //= 10

    while reverse > 0:
        res = reverse % 10
        reverse //= 10
        print(res)


positive_integer(45326)


# Task2
def is_prime_number(number: int) -> bool:
    if type(number) is not int:
        print("Error: Invalid type")
        return False
    if number <= 1:
        return False
    div = 2
    while div < number:
        if number % div == 0:
            return False
        div += 1
    return True


print(is_prime_number(11))


# Task3
def is_lucky_number(number: int) -> bool:
    if type(number) is not int:
        print("Error: Invalid type")
        return False
    if number < 0:
        print("Error: Positive number required")
        return False
    even_sum = 0
    odd_sum = 0
    position = 1
    while number > 0:
        digit = number % 10
        if position % 2 == 0:
            even_sum += digit
        else:
            odd_sum += digit
        position += 1
        number //= 10
    return even_sum == odd_sum


print(is_lucky_number(2322))


# Task4
def count_digits(number: int) -> int:
    if type(number) is not int:
        print("Error: Invalid type")
        return -1
    if number < 0:
        number *= -1
    if number == 0:
        return 1
    count = 0
    while number > 0:
        count += 1
        number //= 10
    return count


print(count_digits(12122))
