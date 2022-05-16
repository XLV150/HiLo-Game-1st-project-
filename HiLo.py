import random

highest = 100
answer = random.randint(1, 100)
guess = 0

print(answer)   # TO SHOW THE RANDOM NUMBER DELETE THIS WHEN YOU WANT ACTUALLY GUESS.

user_guess = int(input("Please guess a number between 1 and {}: ".format(highest)))
guess += 1

if user_guess == answer:
    print("Well done, you got it first try!!!")
elif user_guess > answer:
    print("Please guess lower.")
    guess += 1
else:
    print("Please guess higher.")
    guess += 1

while user_guess != answer:
    user_guess = int(input(""))

    if guess >= 10:
        print("You have exceede 10 guesses, you lose!")
        break
    else:
        if user_guess == 0:
            break
        if user_guess == answer:
            print("Well done, you got it.")
        elif user_guess > answer:
            print("Please guess lower. Or hit 0 to exit")
            guess += 1
        else:
            print("Please guess higher. Or hit 0 to exit")
            guess += 1
