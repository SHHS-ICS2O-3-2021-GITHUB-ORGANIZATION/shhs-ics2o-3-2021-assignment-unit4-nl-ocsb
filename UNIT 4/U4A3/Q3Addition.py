# NAME OF AUTHOR: Nyandea Lansana
# NAME OF THE PROGRAM: Addition Questions
# DATE OF CREATION: Jan. 17, 2022
# PURPOSE OF PROGRAM: To generate two random number between 1 and 100, and display them as additon question. 


# VARIABLE DEFINITION
import random

number1 = 0
number2 = 0

# Input
name = input('Please enter your name: ')
print('Hello ' + name)
print(input(name + ', we have one quick addition question for you. '))

# PROCESSING
number1 = random.randint(1,100)
number2 = random.randint(1,100)
numbsum =  number1 + number2

# OUTPUT 
print("What is the sum of " + str(number1), "and" , str(number2) + "?" )
answer = int(input("Please enter your answer?"))

# Did some else and if statement to the solution of the questions. 
# Programs print out a correct and incorrect statement.

counter = 0
while counter < 5:
  if answer == numbsum: 
    print("Your answer is correct, it is " + str(answer) + "!")
    print(numbsum)
    break
  else:
    print("Your answer is incorrect, please try again.")
    answer = int(input("Please enter your answer?"))
  counter = counter + 1
    