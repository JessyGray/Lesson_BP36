"""
haim() -> Haim, enter amount of apples(by kg)
nastya() ->  Nastya, enter amount of apples(by kg)
alex() -> Alex, enter amount of apples(by kg)
anna() -> Anna, enter amount of apples(by kg)

"""
# def haim():
#     return float(input("Haim, enter amount of apples(by kg)"))
#
#
# def nastya():
#     return float(input("Nastya, enter amount of apples(by kg)"))
#
#
# def alex():
#     return float(input("Alex, enter amount of apples(by kg)"))
#
#
# def anna():
#     return float(input("Anna, enter amount of apples(by kg)"))
#
#
# total=haim()
# total+=nastya()#
# total+=alex()
# total+=anna()
# print(f"Total apples in family {total:.2f} kg")
# print(f"Average for each {total/4:.2f} kg")
count = 0

def haim():
    global count
    count+=1
    return float(input("Haim, enter amount of apples(by kg)"))


def nastya():
    global count
    count += 1
    return float(input("Nastya, enter amount of apples(by kg)"))


def alex():
    global count
    count += 1
    return float(input("Alex, enter amount of apples(by kg)"))


def anna():
    global count
    count += 1
    return float(input("Anna, enter amount of apples(by kg)"))


def moshe():
    global count
    count += 1
    return float(input("Moshe, enter amount of apples(by kg)"))

total=haim()#
total+=nastya()#
total+=alex()
total+=anna()
total+=moshe()
print(f"count = {count}")
print(f"Total apples in family {total:.2f} kg")
print(f"Average for each {total/count:.2f} kg")