total_sum = input("please enter total sum>>>")
cash = input("please enter cash>>>")
name = input("please enter your name>>>")


def change(a: float, b: float, c: str) -> str:
    # <name> your change: <sum>
    return f"{c} your change {(b - a):.2f} NIS"


res = change(float(total_sum), float(cash), name)
print(res)


# res = change(45, "True", 12.6)
# print(res)