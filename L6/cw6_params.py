def func_multy_return():
    return True, 3, 10.7, "hello"


def used_other_func():
    res = func_multy_return()
    print(f"first element with index 0 is {res[0]}")
    print(f"second element with index 1 is {res[1]}")
    print(f"third element with index 2 is {res[2]}")
    print(f"fourth element with index 3 is {res[3]}")
    return res


used_other_func()
print(used_other_func())

def used_other_func(x, x1, x2, x3):
    print(f"first element with index 0 is {x}")
    print(f"second element with index 1 is {x1}")
    print(f"third element with index 2 is {x2}")
    print(f"fourth element with index 3 is {x3}")

res = func_multy_return()
used_other_func(res[0],res[1],res[2],res[3])
