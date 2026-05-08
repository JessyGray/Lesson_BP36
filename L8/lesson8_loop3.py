number = 12345676890
def count_digits(n):
    count = 1
    while n>9:
        count+=1
        n//=10
    return count


print(count_digits(number))
print(count_digits(0))
print(count_digits(9))
print(count_digits(10))