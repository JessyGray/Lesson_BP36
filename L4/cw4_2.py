def f1():
    print("start f1",end="=>")
    f2()
    print("finish f1")


def f2():
    print("start f2",end="=>")
    f3()
    print("finish f2",end="=>")


def f3():
    print("start f3")
    print("finish f3",end="=>")


f1()
