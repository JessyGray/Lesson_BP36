def check_even_or_odd(number:int)->str:
    return "odd" if number%2 else "even"

print(check_even_or_odd(5))
print(check_even_or_odd(6))
print(-11%2)


def always_absolute(number:int)->int:
    return number*-1 if number<0 else number


print(always_absolute(-100))
print(always_absolute(100))