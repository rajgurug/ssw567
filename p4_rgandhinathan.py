#  This script is done by Rajguru Gandhinathan.
#  P4: Guess a Number using loops and a function
import random


#  THe user is importing the random module in this script

#  The comparing function  compares the number to be guessed and guessed number
#  If the number to be guessed and guessed number are same then the function returns 0
#  If the number to be guessed is greater than the guessed number then function returns -1
#  If the number to be guessed is less than the guessed number the function returns 1

def comparing(to_be_guessed, guessed):
    if to_be_guessed == guessed:
        return 0
    elif to_be_guessed > guessed:
        return -1
    else:
        return 1


#  The command random.randint(lower-bound, upper-bound) gives out a random number between lower bound and upper bound
r = random.randint(1, 20)
x = 0

name = input("Hello what is your name?")
print("Well", name, ", I am thinking of a number between 1 and 20")
# A for loop is used to create a loop of 6 times If the comparing function returns 0, the script will print that the
# guessed number was found If the comparing function returns -1, the scrip will print that the guessed number was too
# low If the comparing function returns 1, the script will print that the guessed number was too high If the user
# enters a number greater 20 or less than 1, the script will print that the user needs to give a number between 1 and
# 20. If the user gives non-numeric value, the compiler will ask the user to enter a numeric value between 0 and 20.

i = 0
while i <= 6:
    try:
        num = int(input("Take a guess:"))
    except ValueError:
        print("Enter a numeric value between 1 and 20")
        continue
    m = comparing(r, num)
    if m == 0 and 1 <= num <= 20:
        print("Good job,", name, "! You guessed my number in", i, "guesses!")
        break
    elif m == -1 and 1 <= num <= 20:
        print("your guess is too low")
    elif m == 1 and 1 <= num <= 20:
        print("your guess is too high")
    else:
        print("Give a number between 1 and 20")
    #  Incrementation is done only when numeric values between 0 and 20.
    if 1 <= num <= 20:
        i = i + 1
    if i == 6:
        x = i
#  If user has not guessed the exact number the compiler will print out the guessed number
if x != r:
    print("The number I was thinking of was", r)
