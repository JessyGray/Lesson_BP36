# 5! -> 1-5 1*2*3*4*5 = 120 0!=1
def factorial(number: int) -> int:
    if number <= 1:
        return 1
    return number * factorial(number - 1)


print(factorial(5))
"""
number = 5
factorial(5)->
return 5* factorial(4)
factorial(4)->
return 4*factorial(3)
factorial(3)->
return 3*factorial(2)
factorial(2)->
return 2*factorial(1)
factorial(1)-> return 1
(18)-> return 2*1
(16)-> return 3*2*1
(14)-> return 4*3*2*1
(12)-> return 5*4*3*2*1
"""

print(factorial(0))