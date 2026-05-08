"""
Homework:
1.
   amount of nis from input (ex. 3000)
   rate of dollar from input (ex. 3.003)
   calculate amount of dollars and print it
2.
   total cost of products (ex. 360)
   cash money (ex. 400)
   calculate change and print it

3.advanced
  all values get from input
    hours worked (ex. 182)
    wage (ex. 50)
    tax(%) (ex.11.5 %)
    bonus(%) (ex. 15 %) after tax
    calculate salary netto and print it

"""
# amount_nis = input("amount of nis>>>>")
# rate_of_dollar = input("rate of dollar>>>")
# print(f"{amount_nis} = amount of dollars ${float(amount_nis) / float(rate_of_dollar):.2f}")


# total_cost = input("please enter total cost of products>>>")
# cash_money = input("please enter cash money>>>")
# print(f"your change is {(float(cash_money)-float(total_cost)):.2f} NIS")
# print(39.4==400-360.6)# abs(39.4 - (400-360.6))<0.001
# number = 400-360.6 #1.45*2**11
# print(f"{number:.2f}")
# print(number)

hours_work = input("hours worked>>>")
wage = input("wage>>>")
tax = input("tax(%)>>>")
bonus = input("bonus(%)>>>")
total_salary = float(hours_work) * float(wage)
taxes = float(tax) / 100 * total_salary
salary_after_tax = total_salary - taxes
real_bonus = salary_after_tax * float(bonus) / 100
print(f"salary netto with bonus "
      f"{(salary_after_tax + real_bonus):.2f} NIS")
print(f"salary netto with bonus "
      f"{(float(hours_work)*float(wage)
          *(1-float(tax)/100)*(1+float(bonus)/100)):.2f} NIS")
# %