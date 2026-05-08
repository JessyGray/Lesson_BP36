"""
if condition:
    code
else:
    code
"""
x = 10

def mod(a):
    if a<0:
        a*=-1
    else:
        a=a*10
    return a

print(mod(x))

b = 3
if b==0:
    print(b)
    b+=1
if b==1:
    print(b)
    b+=1
if b==3:
    print(b)
    b+=1
else:
    print("11111")
