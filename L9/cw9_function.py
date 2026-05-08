def count_digit(n:int)->int:
    if type(n) is not int:
        print("please enter integer")
        return -1
    if n < 0:
        n = -n
    if n==0:
        return 1
    res = 0
    while n>0:
        res+=1
        n//=10
    return res


print(count_digit(12345))