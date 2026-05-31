# dictionary key->value
students = {"Anna": 99, "Vadim": 98, "Alex": 100}
print(students)
print(students["Anna"])

students1 = {"Anna": 99, "Vadim": 98, "Alex": 100,"Anna": 98,}
print(students1)
students2 = {"Anna": 100, "Vadim": 100, "Alex": 100}
print(students2)
students1["Anna"]=100
print(students1)
students1["Vera"]=100
print(students1)

# del students1["Alex"]
# print(students1)
print(students1.get("Alex"))
# if "Alex" in students1:
#     del students1["Alex"]
#     print("success")
# else:
#     print("no Alex")
# # del students1["Alex"]
# # print(students1)
# if "Alex" in students1:
#     del students1["Alex"]
#     print("success")
# else:
#     print("no Alex")
#
# print(students1.get("Alex", "no Alex"))

for st in students1:
    print(st)

for st in students1:
    print(students1[st])

for st in students1:
    print(st,students1[st])

#items()

for s, v in students1.items():
    print(s,v)

print(students1.keys())
print(type(students1.keys()))
print(type(students1.values()))
print(type(students1.items()))
students_ = {"Anna":[100,99,98],"Vadim": [98], "Alex": [100,99]}
print(students1.values())


def avg_value(st:dict[str, int])->float:
    if not st:
        return 0.
    return sum(st.values())/len(st)

print(avg_value(students1))
print(avg_value([]))
