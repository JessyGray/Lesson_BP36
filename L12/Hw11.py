# Task6
from shlex import split

text1 = "abcdefgh"
print(text1[2:6])


# Task 9
def check_text_ing(text: str) -> bool:
    return text[-3:] == "ing"


text = input("Enter your text >>>>> ")
print(check_text_ing(text))
# Task 10

text10 = input("Enter text>>>>")
middle = (len(text10) + 1) // 2
print(text10[:middle])
print(text10[middle:])

# Task 11
text = input("Enter name and surname >>> ")

words = text.split(" ")

print(words[1], words[0])

# Task 12
text12 = input("Enter name and surname >>> ")
name = text12.split(" ")
print(name[0][:1], end=". ")
print(name[1])

# Task 13
text13 = input("Enter name and surname>>>")
text13 = text13.lower()
nickname = text13.split(" ")
print(nickname[0][:1], end="")
print(nickname[1][:4])

# Task 14
text13 = input("Enter text>>>")
words = text13.split(" ")
for word in words:
    print(word[::-1], end=" ")

# Task 15
text15 = input("TYPE TEXT >>> ")
words15 = text15.split(" ")
for word in words15:
    print(word[-1] + word[1:-1] + word[0], end=" ")

# Task16
text16 = input("enter your email address>>>")
email = text16.split("@")
stars = len(email[0]) - 2
print(email[0][0], end="")
print(stars * "*", end="")
print(email[0][-1], end="@")
print(email[1])

# Task17
link17 = input("Enter link(https://www...com)>>>")
words17 = link17.split(".")
print(words17[1])

# variant 2
link17 = input("Enter link >>> ")
print(link17[12:-4]
