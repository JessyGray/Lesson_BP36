name = "Alice"
print(type(name))
age = 25
print(type(age))
#1
print("My name is", name, "and my age is", age, "years old")
#2
print("My name is " + name + " and my age is " + str(age) + " years old")
#3 the best
print(f"My name is {name} and my age is {age} years old")
print(f'My name is {name} and my age is {age} years old')

#=================
#4
print("My name is {} and my age is {} years old".format(name,age))
print("My name is {} and my age is {} years old".format(age,name))
# print("My name is {} and my age is {} years old".format(age)) no way
#=================
#5
print("My name is {n} and my age is {a} years old".format(a=age,n=name))

#================= old school
#6
print("My name is %s and my age is %d years old"%(name,age))
"""
%s string
%d integer
%f float

"""
# print("My name is %s and my age is %d years old"%(age, name))
x = 3.000484585739857
print(x)
print(f"{x:.4f}")
# variable : .number of digits after dot f!!! float!!!
y = 213424
print(f"{y:.2f}")