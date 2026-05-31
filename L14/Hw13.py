"""
# Task 1
def sum_odd(num: list[int]) -> int:
    if type(num) is not list:
        print("Error: Invalid type")
        return 0
    res = 0
    for i in num:
        if type(i) is not int:
            print("Error: Invalid type")
            return 0
        if i % 2 != 0:
            res += i
    return res


list1 = [1, 2, 3, 4, 6, -4, -3]
print(sum_odd(list1))




# Task 2
def sum_odd_indx(num: list[int]) -> int:
    if type(num) is not list:
        print("Error: Invalid type")
        return 0
    res = 0
    for i in range(len(num)):
        if type(num[i]) is not int:
            print("Error: Invalid type")
            return 0
        if i % 2 != 0:
            res += num[i]
    return res


list1 = [1, 6, 3, 3, 6, -1, -3]
print(sum_odd_indx(list1))




# Task 3
def max_element(element: list[int]) -> int:
    if type(element) is not list:
        print("Error: Invalid type")
        return 0
    if len(element) == 0:
        print("Error: List can't be empty")
        return 0
    res = element[0]
    for i in range(len(element)):
        if type(element[i]) is not int:
            print("Error: Invalid type")
            return 0
        if element[i] > res:
            res = element[i]
    return res


list1 = [2, 6, 3, 3, 8, -1, -3]
print(max_element(list1))


"""


# Task 4
def even_reverse(numbs: list[int]) -> None:
    if not isinstance(numbs, list):
        print("Error: Invalid type")
        return
    res = []
    for x in reversed(numbs):
        if not isinstance(x, int):
            print("Error: Invalid type")
            return
        if x % 2 == 0:
            res.append(x)
    for x in res:
        print(x, end=" ")


list1 = [2, 4, 5, 3, 8, -1, -3]
even_reverse(list1)


# Task 5
def find_substring(text: str, sub: str) -> int:
    if not isinstance(text, str) or not isinstance(sub, str):
        print("Error: Invalid type")
        return -1
    if len(text) == 0 or len(sub) == 0:
        print("Error: String can't be empty")
        return -1
    if len(sub) > len(text):
        return -1
    return text.find(sub)


print(find_substring("abcde", "cd"))
print(find_substring("abcde", "xy"))
