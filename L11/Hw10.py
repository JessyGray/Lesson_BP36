# Task1
def char_count(text:str,char:str)->int:
    if type(text)is not str or type(char) is not str:
        print("Error: Invalid type")
        return -1
    if len(char)is not 1:
        print("Error:Enter just one character")
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
# Task2
def  print_str_with_space(text1:str)->str:
    if type(text1) is not str:
        print("Error:Invalid type")
        return "Error"
