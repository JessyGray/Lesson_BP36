def first_3(text:str)->None:
    if type(text) is not str:
        print("please enter string")
        return
    print(text[:3])#text[0:3:1]

def last_3(text:str)->None:
    if type(text) is not str:
        print("please enter string")
        return
    print(text[-3:])#text[len(text)-3:len(text):1]


def without_first_last_(text:str)->None:
    if type(text) is not str:
        print("please enter string")
        return
    print(text[1:-1])#text[1:len(text)-1:1]


def every_second_symbol(text:str)->None:
    if type(text) is not str:
        print("please enter string")
        return
    print(text[::2])#text[0:len(text):2]


def reverse_str(text:str)->None:
    if type(text) is not str:
        print("please enter string")
        return
    print(" ".join(text[::-1]))#text[len(text)-1:0:1]


def is_palindrome(text:str)->bool:
    if type(text) is not str:
        print("please enter string")
        return False
    return text.lower()==text[::-1].lower()


def is_palindrome_adv(text:str)->bool:
    if type(text) is not str:
        print("please enter string")
        return False
    clear_text = text.lower().replace(",","").replace(".","").replace(" ","")
    return clear_text==clear_text[::-1]


def is_palindrome_adv_(text:str)->bool:
    if type(text) is not str:
        print("please enter string")
        return False
    clear_text = text.lower().replace(",","").replace(".","").replace(" ","")
    return clear_text==clear_text[::-1]

# str1 = input("please enter string>>>>")
str1 = "  Programming   "
first_3(str1.strip())
last_3(str1.strip())
without_first_last_(str1.strip())
every_second_symbol(str1.strip())
every_second_symbol(123456)
reverse_str(str1.strip())
print(is_palindrome("madam"))
print(is_palindrome("hello"))

print("hello"=="hello")



def phone_hide(text:str)->str:
    if type(text) is not str:
       return "please enter string"
    if not text.isdigit():
        return "please enter only digits"
    if len(text)<8 or len(text)>18:
        return "wrong data"
    return "*"*(len(text)-4) + text[-4:]


print(phone_hide("12345678"))

