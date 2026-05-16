text1 = ('hello'
         'group')
text2 = ("hello"
         "group")
text3 = """hello
        group"""
print(text1)
print(text2)
print(text3)

text4 = "hello group 36!!_"
print(len(text4))  # string length
print(text4[0])
print(text4[16])
# print(text4[17])
print(text4[-1])
print(text4[-17])
# print(text4[-18])
# lower upper
print(text4.upper())
print(text4)
text5 = text4.upper()
print(text5)
text6 = "   text text   "
# strip javascript trim
login = "text text"
print(text6)
print(text6 == login)
print(text6.strip() == login)

# replace
print(text6.replace("text", "group"))
print(text6)

str1 = "hello"
print(id(str1))
str2 = str1
print(id(str2))
str1 = str1 + "!!!!"
print(id(str1))
print(str1)
print(id(str2))
print(str2)

# split delimiter
words = text4.split(" ")
print(words)
str3 = "/".join(words)
print(str3)
print(str3.find("/3"))
print(str3.find("?3"))

"""
isdigit only digits?=>true
isalpha only letters?=>true
isalnum only digits and letters?=>true
isspace only spaces?=>true
"""
print("12345".isdigit())
print("12345".isalpha())
print("12345".isalnum())
print("12345".isspace())
print("      ".isspace())


# "12344" "-1234"
def is_int(number: str) -> bool:
    if type(number) is not str or number.strip() == "":
        return False
    if number[0] == "-" and len(number) == 1:
        return False
    index = 1 if number[0] == "-" else 0

    while index < len(number):
        if not number[index].isdigit():
            return False
        index += 1

    return True


def count_digits(number: int | str) -> int:
    if type(number) is str and is_int(number):
        number = int(number)
    if type(number) is not int:
        print("Error: number must be an integer.")
        return -1
    if number < 0:
        number = -number
    if number == 0:
        return 1
    count = 0
    while number > 0:
        count += 1
        number //= 10
    return count


print(count_digits("-1234"))


def count_digits_adv(number: int | str) -> int:
    if type(number) is int:
        number = str(number)
    elif type(number) is str:
        number = number.strip()
        if not is_int(number):
            return -1
    else:
        return -1
    return len(number)-1 if number[0]=="-" else len(number)

print(count_digits_adv("-1234"))


str5 ="Hello sveta"
words1 = str5.strip().lower()
print(words1.find("Sveta".lower()))
print("===========")
print(len(str(12345)))

