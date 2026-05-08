import random


def guess_number():
    target = random.randint(1, 10)
    guess = 0
    while guess != target:
        guess = input("Please enter number from 1 till 10 or cancel>>>")
        if guess == "cancel":
            break
        test = int(guess)
        if test < target:
            print("to small")
        elif test > target:
            print("to big")
        else:
            print("Win!")
            break


guess_number()