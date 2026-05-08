def delay_on_city(city: str) -> int:
    if not isinstance(city, str):
        raise TypeError("City must be string")

    match city:
        case "Jerusalem":
            return 20
        case "Tel-Aviv":
            return 35
        case "Beer-Sheva":
            return 15
        case "Haifa":
            return 25
        case _:
            raise ValueError("Wrong city")


def delay_on_year(year: int) -> int:
    if not isinstance(year, int):
        raise TypeError("Year must be integer")

    if year < 1950 or year > 2026:
        raise ValueError("Wrong year")

    if year <= 1995:
        return 15
    if year <= 2005:
        return 10
    if year <= 2017:
        return 5

    return 0


def delay_time(hour: int) -> int:
    if not isinstance(hour, int):
        raise TypeError("Hour must be integer")

    if hour < 0 or hour >= 24:
        raise ValueError("Wrong time")

    match hour:
        case h if 7 < h <= 9:
            return 20
        case h if 9 < h < 11:
            return 10
        case h if 11 <= h < 13:
            return 5
        case _:
            return 0


def time_on_route(pure_time: int, hour: int, city: str, year: int) -> int:
    if not isinstance(pure_time, int):
        raise TypeError("Pure time must be integer")

    if pure_time <= 0:
        raise ValueError("Pure time must be positive")

    return (
        pure_time
        + delay_time(hour)
        + delay_on_city(city)
        + delay_on_year(year)
    )


tests = [
    (45, 10, "Jerusalem", 2025),
    (-10, 10, "Jerusalem", 2025),
    (45, 25, "Jerusalem", 2025),
    (45, -25, "Jerusalem", 2025),
    (45, 20, "Jeru", 2025),
    (45, 2, "Jerusalem", 1000),
    (45, 2, "Jerusalem", 2030),
    ("45", 2, "Jerusalem", 1000),
    (55, 7, "Tel-Aviv", 1990),
]

for pure_time, hour, city, year in tests:
    try:
        result = time_on_route(pure_time, hour, city, year)
        print(f"Time on route {result // 60} hour {result % 60} min")
    except (TypeError, ValueError) as error:
        print(f"Error data: {error}")
