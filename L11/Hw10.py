# Task1
def char_count(text:str,char:str)->int:
    if type(text)is not str or type(char) is not str:
        print("Error: Invalid type")
        return -1
    if text == "" or char == "":
        print("Error: Text or Char can't be empty")
        return -1
    if len(char) != 1:
        print("Error: Enter just one character")
        return -1
    count=0
    digit=0
    length=len(text)
    while length>0:
        if char==text[digit]:
            count+=1
        digit+=1
        length-=1
    return count

print(char_count("Hellloo","l"))

# # Task2
def  print_str_with_space(text1:str)->None:
    if type(text1) is not str:
        print("Error:Invalid type")
        return
    ser=0
    while ser< len(text1):
        print(text1[ser],end=" ")
        ser+=1


print_str_with_space("hello")
print()

# Task3
def reverse_number(num: int) -> None:
    if type(num) is not int:
        print("Error: Invalid type")
        return
    if num<0:
        num*=-1
    num = str(num)
    length1 = len(num) - 1
    while length1 >= 0:
        print(num[length1], end=" ")
        length1 -= 1


reverse_number(1234)
