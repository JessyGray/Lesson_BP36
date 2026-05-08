def schedule_work(week):
    if type(week) != int:
        return "Error: invalid type. Please enter integer"
    if week<=0 or week>52:
        return "Error: wrong value"
# Anna Vera Vadim Daniel
    match week%4:
        case 1:
            return "Anna"
        case 2:
            return "Vera"
        case 3:
            return "Vadim"
        case 0:
            return "Daniel"
        case _:
            return "Very strange"


print(schedule_work(53))
print(schedule_work(10))
print(schedule_work(13))
print(schedule_work(0))