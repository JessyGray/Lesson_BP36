s = "hello world"
print(s[4])
print(s[10])
print(s[len(s) - 1])
print(s[-1])
for ch in s:
    print(ch)

# tuple
t1 = (4, 12, -7, 3, 24)
t2 = 4, 12, -7, 3, 24
print(len(t1))
print(len(t2))
for x in t2:
    print(x)

print(t2[2])
print(type(t1))
print(type(t2))

# list
l1 = [4, 12, -7, 3, 24]
print(type(l1))
print(len(l1))
for x in l1:
    print(x)

l2 = []
print(l2)
l2.append(1)
l2.append(4)
print(l2)
l3 = list(t1)
print(l3)
print(t1)
l3.append(5)
print(l3)
t3 = ()
l4 = list("hello world")
print(l4)
l3[4] = 1000
print(l3)
# t1[4]=1000
# print(t1)

t4 = tuple(l3)
print(t4)
l3.sort()
print(l3)

t5 = [1, 2, 3], [3, 4, 5], [6, 7, 8]
# ref#list1 ref#list2 ref#list3
print(t5)
t5[0][1] = 1000
print(t5)
t5[0].append(1000)
print(t5)
list1 = [1, 2, 3]
list2 = [3, 4, 5]
list3 = [6, 7, 8]
t6 = list1, list2, list3
print(t6)
print(id(list1))
list1.append(1000)
print(id(list1))
# t6[0]=list2
for i in range(100):
    list1.append(i)
print(id(list1))
list4 = list(range(10))
print(list4)
# list comprehension
list5 = [i for i in range(10)]
print(list5)
print(list1)
list6 = [i for i in range(10) if i % 2 == 0]
print(list6)
list7 = [-1] * 10
print(list7)
"""
[] [1,6,9,12]
str tuple range => list()
append()
list comprehension
[x]*n
"""


# print(t6)

def sum_even(arr: list[int]) -> int:
    if type(arr) is not list:
        return 0
    res=0
    for num in arr:
        if num%2==0:
            res+=num
    return res

print(sum_even(list1))
print(sum_even(list6))
print("="*30)
for x  in list6:
    print(x)
else:
    print("finish")

def sample(arr:list[int])->None:
    for x in arr:
        print(x)
        if x==10:
            break
    else:
        print("finish")


sample(list6)

# enumerate()
# for n in nums: elements
# for i in range(len(nums)): indexes
nums = [9, 11, 4, -1, 8, -4, 30, 2]
nums1 = [9, True, 4, -1, 8, -4, 30, 2]
nums2 = [9, 11, 4, -1, "hello", -4, 30, 2]
# for i, n in enumerate(nums):
#     print(i , "->" , n)
nums3 = [-10, -100, -1000]
