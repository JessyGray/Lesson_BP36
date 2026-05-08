def num_7_to_binary():
    number =7
    div_ = number%2 # 1
    temp = number//2 #3
    print(div_)
    if temp==0:
        return
    div_ = temp % 2 # 1
    temp = temp//2 #1
    print(div_)
    if temp==0:
        return
    div_ = temp % 2 # 1
    temp = temp//2 #0
    print(div_)
    if temp==0:
        return

num_7_to_binary()

print("===========loop=========")
# while condition => True
#           code
# if condition False

def num_7_to_binary():
    number = 7
    while number!=0:
        print(number%2)
        number//=2

num_7_to_binary()