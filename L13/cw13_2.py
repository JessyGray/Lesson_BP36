
# reversed()
def print_reverse(arr:list[int])->None:
    for x in reversed(arr):
        print(x, end=" ")
    print()

list6 = [i for i in range(10) if i % 2 == 0]
tuple1 = tuple(list6)
print(list6)
print_reverse(list6)
print(list6)
print(reversed(list6))
print(list(reversed(list6)))

#reverse()
list6.reverse()
print(list6)

def print_reverse(arr:tuple[int])->None:
    for x in reversed(arr):
        print(x, end=" ")
    print()

print_reverse(tuple1)
# tuple1.reverse()

