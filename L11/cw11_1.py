# slices string[start:stop:step]
"""
start - index from (default = 0)include
stop index finish (not include) default = len(string)
step - default = 1
"""
str1 = "Hello group 36 and welcome"
print(str1[:])
print(str1[:7])
print(str1[7:])
print(str1[7:12])
print(str1[::2])
print(str1[3:15:2])

print(str1[::-1])
print(str1[-len(str1)])

def get_start():
    return 4

print(str1[get_start()::2])
print(str1[:100:2])
# print(str1[100])
# print(str1[::0])
print(str1[-10:-1])
print(str1[-1:-10:-1])




