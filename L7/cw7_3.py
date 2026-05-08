"""
try -> code
except
else

raise

"""

# try:
#     number = int(input("Enter number>>>"))
#     print(number)
# except:
#     print("Something wrong")
# number = int(input("Enter number>>>"))

# try:
#     number = int(input("Enter number>>>"))
#     print(number)
# except ValueError:
#     print("Something wrong")
#     number = int(input("Enter number>>>"))
#     print(number)


#else
try:
    number = int(input("Enter number>>>"))
    print(number)
except ValueError:
    print("Something wrong")
else:
    print(number/10)

#raise




