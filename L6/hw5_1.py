"""
Task 2: Salary Calculation (Netto)
Objective:
Create a function called salary(). This function will calculate the net salary of a person after tax deduction. The function should:
1.	Prompt the user to enter the number of working hours.
2.	Ask for the hourly wage.
3.	Request the tax percentage.
Goal:
•	Calculate the gross salary by multiplying hours by wage.
•	Deduct the tax to calculate the net salary.
•	Return the net salary.
•	Use the function to calculate the net salary for Nastya and Alex.
salary()
"Enter hours>>>"
"Enter wage>>>"
"Enter tax(%)>>>>"
function should return salary netto
calaculate salary for Nastya and Alex

"""
#
# def salary():
#     hours_work = input("hours worked>>>")
#     wage = input("wage>>>")
#     tax = input("tax(%)>>>")
#     total_salary = float(hours_work) * float(wage)
#     taxes = float(tax) / 100 * total_salary
#     salary_after_tax = total_salary - taxes
#     return  salary_after_tax
#
#
# print("Nastya, please")
# res = salary()
# print(f"Salary netto Nastya: {res:.2f} ")
# print("Alex, please")
# res = salary()
# print(f"Salary netto Alex: {res:.2f} ")

def salary(name):
    hours_work = input(f"{name} hours worked>>>")
    wage = input(f"{name} wage>>>")
    tax = input(f"{name} tax(%)>>>")
    total_salary = float(hours_work) * float(wage)
    taxes = float(tax) / 100 * total_salary
    salary_after_tax = total_salary - taxes
    return  salary_after_tax, name



res = salary("Nastya")
print(f"Salary netto for {res[1]}: {res[0]:.2f} ")
res1 = salary("Alex")
print(f"Salary netto for {res1[1]}: {res1[0]:.2f} ")
print(f"Total salary for")
