def delay_time(hour):
    if hour < 0 or hour >= 24:
        print("Wrong time")
        return -1
    if 7 < hour <= 9:
        delay = 20
    elif 9 < hour < 11:
        delay = 10
    elif 11 <= hour < 13:
        delay = 5
    else:
        delay = 0
    return delay

def delay_time_python(hour):
    if hour < 0 or hour >= 24:
        print("Wrong time")
        return -1
    match hour:
        case h if 7 < h <= 9:#case _ if 7 < hour <= 9
            delay = 20
        case h if 9 < h < 11:
            delay = 10
        case h if 11 <= h < 13:
            delay = 5
        case _:
            delay = 0
    return delay


def delay_on_city(city):
    match city:
        case "Jerusalem":
            delay = 20
        case "Tel-Aviv":
            delay = 35
        case "Beer-Sheva":
            delay = 15
        case "Haifa":
            delay = 25
        case _:
            print("Wrong city")
            delay = -1
    return delay


def delay_on_year(year):
    if year<1950 or year>2026:
        print("Wrong year")
        return -1
    if year <=1995:
        return 15
    if year<=2005:
        return 10
    if year<=2017:
        return 5
    return 0



def time_on_route(pure_time: int, hour: int, city: str, year: int) -> int:
    if type(hour) is not int or type(pure_time) is not int or type(year) is not int or type(city) is not str:
        print("Error: invalid type")
        return -1
    delay_time_var = delay_time(hour)
    delay_on_city_var = delay_on_city(city)
    delay_on_year_var = delay_on_year(year)
    if pure_time <= 0 or delay_time_var < 0 or delay_on_city_var < 0 or delay_on_year_var < 0:
        return -1
    return pure_time + delay_time_var + delay_on_year_var + delay_on_city_var


res_ = time_on_route(45, 10,"Jerusalem",2025)
print("Error data" if res_<0 else f"Time on route {res_//60} hour {res_%60} min")

res_ = time_on_route(-45, 10,"Jerusalem",2025)
print("Error data" if res_<0 else f"Time on route {res_//60} hour {res_%60} min")

res_ = time_on_route(45, 100,"Jerusalem",2025)
print("Error data" if res_<0 else f"Time on route {res_//60} hour {res_%60} min")


res_ = time_on_route(45, 12,"Tel-Aviv",2000)
print("Error data" if res_<0 else f"Time on route {res_//60} hour {res_%60} min")
#Ternary operator
"""
expression if true<= condition =>false else expression
"""