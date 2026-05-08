# if
"""
if condition:
    code-> if condition==True
if condition False - here
"""
a = 100
if a == 10:
    print("a=10")
print("game over")
"""
       <8 -> sleep
       >=8 and <17 -> work
       >=17 and <22 -> rest
       """


def schedule(time: int) -> str:
    if time < 8:
        return "sleep"
    if 8 <= time < 17:
        return "work"
    if 17 <= time < 22:
        return "rest"
    return "sleep"


def schedule(time: int) -> str:
    if type(time)!=int:
        return "error type"
    if time < 0 or time > 23:
        return "error time"
    if time < 8 or time >= 22:
        return "sleep"
    if time < 17:
        return "work"
    return "rest"



print(schedule(10))
print(schedule(5))
print(schedule(23))
print(schedule(20))
print(schedule(25))
print(schedule(-20))
print(schedule("one"))