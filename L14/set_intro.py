numbers = [10, 2, 2, 4, 4, 7, 7, 8]
tuple1 = (1, 2, 3, 4, 5)
set1 = set(numbers)
print(set1)
set2 = {1, 2, 3, 4}
print(type(numbers))
print(type(tuple1))
print(type(set1))
print(type(set2))
set_ = {}
print(type(set_))
set3 = set()
print(type(set3))
print(numbers[0])
print(tuple1[0])
# print(type(set1[0]))
print(set1.add(100))
print(set1)
print(set1.add(100))
print(set1)
print(set1.add(100))
# print(set1.remove(100))
# print(set1)
# print(set1.remove(100))
# print(set1)
print(set1.discard(100))
print(set1)
print(set1.discard(100))
print(set1)
if 10 in set1:
    print("hurraaa")
else:
    print("pity")
if 100 in set1:
    print("hurraaa")
else:
    print("pity")

set_1 = {"Anna", "Vera", "Oleg"}
set_2 = {"Alex", "Anna", "Oleg"}
# common
common = set_2 & set_1
print(common)
# all_students
all_students = set_1 | set_2
print(all_students)
# only
only_set1 = set_1 - set_2
print(only_set1)
only_set2 = set_2 - set_1
print(only_set2)
"""
list mutable indexes
tuple immutable indexes 
set unique elements no indexes
"""
print(len(set1))


def lucky_remove(set_: set[int], element: int) -> bool:
    len_old = len(set_)
    set_.discard(element)
    return len_old != len(set_)


print(lucky_remove(set1, 10))
print(lucky_remove(set1, 10))

print(set1)
print(set2)
set1.update(set2)
print(set1)