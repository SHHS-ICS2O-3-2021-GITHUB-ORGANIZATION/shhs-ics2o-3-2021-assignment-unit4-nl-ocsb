# NAME OF AUTHOR: Nyandea Lansana
# NAME OF THE PROGRAM: Guessing Game 
# DATE OF CREATION: Jan. 25, 2022
# PURPOSE OF PROGRAM: To create a fun and engaging number game where the program guess a number between the minimum and maximum value entered by the user.  

# Program Title
print ("Number Guessing Game")

# importing a time module so it exucutes swiftly instead
# of in a clustered way.
import time

time.sleep(2)
# some information about what the game  
# and how to use it
print("\nHello there, user! This tool allows you to enter two integers and it will produce a random number that falls between the two. Your job is to figure out which number the tool picked. It will initially request a lower bound, which will be the first number you enter. Additionally, it asks for an upper bound, which is the second number you want to use. In a nutshell, the lower and upper bounds refer to the range of numbers you want to try and guess accurately. After that, the tool will ask you to guess the two numbers you typed in. Along the way, you'll get suggestions that will tell you if you're guessing too high or too low. When you accurately identify the number that the programme predicted, it will notify you and tell you how many attempts it took. So, what exactly are you waiting for? Try it out and have a good time. You just finished reading my entire essay when all you wanted to do was play the game, therefore you deserve to have a good time.")

# importing a random module so that the numbers are randomize
import random

# VARIABLE DEFINITION
# initializing the number of guesses 
guessestaken = 0

# INPUT

time.sleep(4)
username = input("\nWelcome to Guess The Number! What is your name? ")

# taking input for the range the user want
# lowerbound as in a minimum value
# upperbound as in a maximum value
minimum = int(input("\nEnter in an integer for a lower bound:"))
maximum = int(input("Enter in an integer for an upperbound:"))

# making the program take a guess between that input 
# from the minimum and maximum value
secretnumber = random.randint(minimum, maximum)

# let the user know that the program has store a secret number 
# between the two numbers that they entered
print("\nWell, " + username + ", I am thinking of a number between " + str(minimum) + " and " + str(maximum)  + ". Take a guess and let the game begin!")

# PROCESSING & OUTPUT
while True:
    guessestaken += 1
 
    # taking guessing number as input
    usersguess = int(input("\nWhat is your guess?"))

    # condition testing with else and if statements
    if secretnumber == usersguess:
        print("Congratulations",username,", you did it in",guessestaken,"attempt(s)")
        # once the user gets it, the loop will break
        break
    # helping the user with appropriate feedback so they know
    # what they're doing wrong 
    elif secretnumber > usersguess:
        print("You guessed too small! You got this try again.")
    elif secretnumber < usersguess:
        print("You Guessed too high! It's okay to aim higher, but maybe just go a little lower.")