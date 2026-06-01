def lucky_remove(set_: set[int], element: int) -> bool:
    try:
        set_.remove(element)
        return True
    except:
        return False


numbers = [10, 2, 2, 4, 4, 7, 7, 8]
set1 = set(numbers)

print(lucky_remove(set1, 10))
print(lucky_remove(set1, 10))


# 2
def avg_value(st: dict[str, int]) -> float:
    res = 0
    for value in st.values():
        res += value
    return res / len(st)


students1 = {"Anna": 99, "Vadim": 98, "Alex": 100}
print(f"{avg_value(students1):.2f}")
