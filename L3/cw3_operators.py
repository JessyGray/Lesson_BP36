"""
arithmetics operators
+ addition 5+4 = 9
- subtraction 5-4 = 1
* multiplication 5*4 = 20
/ division 10/4 = 2.5
// floor division 10//4 = 2
% modulo 10%3 = 1 10 = 3*3+1
** exponentiation 2**3 = 8
"""
# print(5+10)
# print(5*10)
# print(5//10)

"""
== equal to 
!= not equal to
> greater than
< less than
>= greater than or equal to
<= less than or equal to
"""
# print(6==6)
# print(6==7)
# print(6!=7)
# print(6<=7)
"""
logical operators
and 

op1     op2     result
True    True    True
False   True    False
True    False   False
False   False   False

or

op1     op2     result
True    True    True
False   True    True
True    False   True
False   False   False

not
not True => False
not False => True
"""
# print(5==5 and 5>4)
# print(5==5 and 5<4)
#
# print(5==5 or 5<4)

"""
assignments operators

= assignment x = 10
+= addition and assignment
-=
/=
*=
//=
%=
**=
"""
x = 10
# 10 =x no way
x += 10  # x = x+10
# print(x)
x += 1
# x++
"""
1)0  False
2)9%3!=3 True
3)2==2 True
4)12<14 True
5)-1 True


1)0 or 1 True
2)1 or 1 True
3)0 or 0 False
4)0 and 1 False
5)not (0 and 1)
"""

print(bool(0))
print(9 % 3 != 3)
print(2 == 2)
print(12<14)
print(bool(-1))

"""
False:
False
0
""
[]
{}
set()
None
"""
print(bool(""))
print(bool(" "))



print(1 or 2 or 3 or 10)
print(1 or 1)

print(0 or 1)
print(1 or 0)
print(0 or 0)

print(not (0 and 1))

""""
not (x and y) or (not x and y)

1)x=0, y =1; True
2)x=1, y =0; True
3)x=1, y =-1; False
4)x=0, y =-5; True
5)x=0, y =0; True
"""

print(not (0 and 1) or (not 0 and 1)) #not(False)=>True
print(not (1 and 0) or (not 1 and 0)) #not(False)=>True
print(not (1 and -1) or (not 1 and -1)) #not(True)=>False or (False and True)=>False
print(not (0 and 0) or (not 0 and 0))#not(False)=>True

print(1 and 3 and 2 and 10)
print(1 and 3 and 0 and 10)

"""
Homework:
1.
   amount of nis from input (ex. 3000)
   rate of dollar from input (ex. 3.16)
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
