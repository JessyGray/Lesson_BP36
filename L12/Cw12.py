
"""
for element in iterable:
    code
"""

text = "hello my group"
for ch in text:#for each
    print(ch.upper())

def count_symbol(text: str, ch:str)->int:
    if type(text) is not str:
        return -1
    if type(ch) is not str:
        return -1
    if text.strip()=="":
        return -1
    if len(ch)!=1:
        return -1
    count = 0
    char=ch.lower()
    for s in text:
        if s.lower()==char:
            count+=1
    return count

print(count_symbol("hello my grOup","o"))

def reverse_text(text:str)->str:
    if type(text) is not str or text.strip()=="":
        return "Error: please enter correct string"
    reverse_ = ""
    for i in range(len(text)-1,-1,-1):
        reverse_+=text[i]
    return reverse_

print(reverse_text(text))

def is_palindrome(text:str)->bool:
    if type(text) is not str or text.strip()=="":
        return False
    temp = text.lower().strip().replace(" ","")
    for i in range(len(temp)//2):
        if temp[i]!=temp[len(temp)-1-i]:
            return False
    return True

print(is_palindrome("123454321"))
print(is_palindrome("1234564321"))
# ___________________________________
#range()
print(range(5))
#range(start, stop, step)
# 1 argument -> stop
# 2 arguments -> start and stop
# 3
for i in range(5):
    print(i)


text = "fasdkfj ewr flkj ernzlk"
# for ch in text:
#     print(ch)


for i in range(10,19,2):
    print(text[i])




str1 = "1234567"


str2 = str1[1:7]
print(str2)
for i in range(len(str1)):
    print(int(str1[i])**2)


print("-"*10)
for i in range(1,7,2):
    print(int(str1[i]) ** 2)
