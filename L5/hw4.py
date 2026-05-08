def f6():
    print("f6()")


def f5():
    print("f5()",end=" ")
    f6()


def f4():
    print("f4()", end=" ")
    f5()


def f1():
    print("f1()",end=" ")
    f4()


def f2():
    print("f2()",end=" ")
    f6()


def f3():
    print("f3()")


def main():
    print("main", end=" ")
    f6()
    print("main", end=" ")
    f1()
    print("main", end=" ")
    f2()


main()

