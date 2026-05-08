"""
main f4
main f1 f3 f5
main f2 f6 f5
"""


def f4():
    print("f4")


def f5():
    print("f5")


def f3():
    print("f3", end=" ")
    f5()


def f1():
    print("f1", end=" ")
    f3()


def f6():
    print("f6", end = " ")
    f5()


def f2():
    print("f2", end=" ")
    f6()


def main():
    print("main", end=" ")
    f4()
    print("main", end=" ")
    f1()
    print("main", end=" ")
    f2()


main()