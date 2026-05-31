# Task 1
"""
def has_subnumber(number: int, sub: int) -> int:
    if type(number) is not int or type(sub) is not int:
        print("Error: Invalid type")
        return -1
    if number < 0 or sub < 0:
        print("Error: numbers must be non-negative")
        return -1
    number = str(number)
    sub = str(sub)
    count = 0
    for i in range(len(number) - len(sub) + 1):
        if number[i:i + len(sub)] == sub:
            count += 1
    return count


print(has_subnumber(1212121, 121))




# Task 2
def count_digit_in_range(n: int, d: int) -> int:
    if type(n) is not int or type(d) is not int:
        print("Error: Invalid type")
        return -1
    if n < 0 or d < 0:
        print("Error: numbers must be non-negative")
        return -1
    if d > 9:
        print("Error: d must be digit from 0 to 9")
        return -1
    d = str(d)
    count = 0
    for i in range(n + 1):
        i = str(i)
        for c in i:
            if c == d:
                count += 1

    return count


print(count_digit_in_range(52, 1))

print(count_digit_in_range(123, 1))




# Task 3
def replace_subnumber(number: int, sub: int, rep: int) -> int:
    if type(number) is not int or type(sub) is not int or type(rep) is not int:
        print("Error: Invalid type")
        return -1
    if number < 0 or sub < 0 or rep < 0:
        print("Error: numbers must be non-negative")
        return -1
    number = str(number)
    sub = str(sub)
    rep = str(rep)
    result=""
    i=0
    while i<len(number):
        if number[i:i+len(sub)]==sub:
            result+=rep
            i+=len(sub)
        else:
            result+=number[i]
            i+=1
    return int(result)

print(replace_subnumber(120120120,0,5))
# Skazali chto loop nado ispolzovat, poetomu replace ne ispolzoval


# Task 4
def normalize_spaces(text: str) -> str:
    if type(text) is not str:
        return "Error: Invalid type. Enter str"
    text = text.split()
    text = " ".join(text)
    return text


print(normalize_spaces("   Hello     Group             BP36  "))

"""


# Task 5
def are_anagrams(s1: str, s2: str) -> bool:
    if type(s1) is not str or type(s2) is not str:
        print("Error: Invalid type. Enter str")
        return False
    s1_l = s1.lower().replace(" ", "")
    s2_l = s2.lower().replace(" ", "")
    if len(s2_l) > len(s1_l):
        return False
    for i in s2_l:
        letter=s1_l.find(i)
        if letter==-1:
            return False
        s1_l=s1_l[:letter]+s1_l[letter+1:]
    return True
print(are_anagrams("hello", "ole"))      # True
print(are_anagrams("helo", "hello"))     # False
print(are_anagrams("Ha Le Lu Ya", "LAH")) # True
"""
ana
=======
a---> use / delete>>>next ==== na
n---> use / delete>>>next =====a
a---> use / delete>>>next -


=======
anama


"""
