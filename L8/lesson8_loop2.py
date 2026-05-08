# x = 0
# while x < 5:
#     print(x)
#     x += 1


def check_password():
    password = "complicated_password"
    pass_=""
    count = 0
    while pass_!=password:
        pass_= input("Please enter password>>>")
        count+=1
        if count==3:
            break
    else:
        print("successful")
    print("access denied")


# check_password()

a = 0
while a<10:
    a+=1
    if a%2:
        continue
    print(a)