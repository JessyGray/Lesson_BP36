# Task 1 - a
def delaytime(hour: int) -> int:
    if type(hour) is not int:
        print("Wrong type")
        return -1
    if hour < 0 or hour > 23:
        print("Wrong time")
        return -1
    if 7 <= hour <= 9:
        return 20
    elif 9 < hour < 11:
        return 10
    elif 11 <= hour < 13:
        return 5
    else:
        return 0


delay = delaytime(9)
print(delay)
delay = delaytime(-6)
print(delay)
delay = delaytime("a")
print(delay)


# Task 1 - b
def delayOnCity(city: int) -> int:
    if type(city) is not int:
        print("Wrong type")
        return -1
    match city:
        case 1:
            return 20
        case 2:
            return 35
        case 3:
            return 15
        case 4:
            return 25
        case _:
            print("Wrong city")
            return -1


delaycity = delayOnCity(1)
print(delaycity)

delaycity = delayOnCity(5)
print(delaycity)

delaycity = delayOnCity("a")
print(delaycity)


# Task 1 - c
def delayOnYear(year: int) -> int:
    if type(year) is not int:
        print("Wrong type")
        return -1
    if year < 1950 or year > 2024:
        print("Wrong year")
        return -1
    if year <= 1995:
        return 15
    elif 1995 < year <= 2005:
        return 10
    elif 2005 < year <= 2017:
        return 5
    else:
        return 0


delayyear = delayOnYear(1990)
print(delayyear)

delayyear = delayOnYear(2000)
print(delayyear)

delayyear = delayOnYear(2010)
print(delayyear)

delayyear = delayOnYear(2020)
print(delayyear)

delayyear = delayOnYear(1800)
print(delayyear)

delayyear = delayOnYear("a")
print(delayyear)


# Task 2
def timeOnRoute(pureTime: int, hour: int, city: int, year: int) -> int:
    if type(pureTime) is not int:
        print("Wrong type")
        return -1
    x = delaytime(hour)
    y = delayOnCity(city)
    z = delayOnYear(year)
    if x == -1 or y == -1 or z == -1:
        return -1
    return pureTime + x + y + z


res = timeOnRoute(100, 8, 1, 2010)
print(res)

res = timeOnRoute(120, 10, 2, 2000)
print(res)

res = timeOnRoute(90, 12, 3, 2020)
print(res)

res = timeOnRoute(80, 5, 4, 1990)
print(res)

res = timeOnRoute(100, -1, 1, 2010)
print(res)

res = timeOnRoute(100, 8, 5, 2010)
print(res)

res = timeOnRoute(100, 8, 1, 1800)
print(res)

res = timeOnRoute(100, "a", 1, 2010)
print(res)