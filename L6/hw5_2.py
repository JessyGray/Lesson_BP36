def salary_adv(name):
    hours_work = input(f"{name} hours worked>>>")
    wage = input(f"{name} wage>>>")
    tax = input(f"{name} tax(%)>>>")
    bonus = input(f"{name} bonus(%)>>>")
    return salary(float(hours_work), float(wage), float(tax), float(bonus)), name


def salary(hours_work, wage, tax, bonus):
    return hours_work * wage * (1 - tax / 100) * (1 + bonus / 100)


# res = salary_adv("Nastya")
# print(f"Salary netto for {res[1]}: {res[0]:.2f} ")
# res1 = salary_adv("Alex")
# print(f"Salary netto for {res1[1]}: {res1[0]:.2f} ")


def function():
    return 1, 2, 3, "hello"


print(function())

"""
 0  1  2    3
(1, 2, 3, 'hello')
"""
res = function()
print(res[3])
