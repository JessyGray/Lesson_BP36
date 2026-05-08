a = 10

def f1():
    print(a)

a=100
f1()


def f2():
    a = 15
    print(a)

f2()
print(a)

def f3():
    b = 125
    print(b)
    return b


f3()
# print(b)
print(f3())


def f4():
    b = a+10
    print(b)


f4()

def f5():
    global a
    a = a+10


f5()
print(a)


def f6():
    global a
    a = "hello"


f6()
print(a)