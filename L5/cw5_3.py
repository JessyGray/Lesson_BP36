def sum_(a: int, b: int) -> int:
    return a + b


x = 10
y = 15
print(sum_(x, y))
print(sum_(123, 45))
print(sum_("hello ", "group 36"))


def multy_sum(a, b, c, d):
    return a + b + c + d


print(multy_sum(12, 7, 90, 12))

print(multy_sum(d=15, a=12, c=45, b=1))
print(multy_sum(15,30,d=4, c=10))
print(multy_sum(d=15, a=12, c=45, b=1))
print(multy_sum(15,30,c=4, d=10))
# print(multy_sum(c=4, d=10, 10,15))

def sub(a = 0,b = 0):
    return a-b

print(sub(b = 10, a = 15))
print(sub(10, 15))


def greeting(name = "strange"):
    print(f"Hello {name}")


greeting()
greeting("Svetlana")


print(sub())