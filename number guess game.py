print("Welcome to the world of guessing numbers")
print("Are you genius in guessing?")
import random
top_range = input("Type a number: ")
if top_range.isdigit():
    top_range = int(top_range)
    if top_range <= 0:
        print("please type number greater than 0")
        quit()
else:
    print("please text number next time")
random_number = random.randint(0,top_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("please type a number")
        continue
    if user_guess == random_number:
        print("You got it!")
        break
    elif user_guess > random_number:
        print("You are above the number")
    else:
        print("You are below the number")
print("You got it in " + str(guesses) + " guesses")

