# NAME OF AUTHOR: Nyandea Lansana
# NAME OF THE PROGRAM: Random Range 
# DATE OF CREATION: Jan. 17, 2022
# PURPOSE OF PROGRAM: To create a code where the program accept two variables from a user, and proceeds to give an output that's a random number between the range given by the user.

# VARIABLE DEFINITION

#Using randint method to get a random integers.  
import random
number1 = 0
number2 = 0
randnumb1 = 0

# INPUT
# Some user friendly prompts. 
name = input('Please enter your name: ')
print('Hello ' + name)

number1 = int(input("Please enter the first number and let it be smaller than you second number:"))
number2 = int(input("Please enter the second number and let it greater than you first number:")) 

# PROCESSING
# Assigning the answer to the random randint method for a range between the user's input
randomnumb1 = random.randint(number1, number2)

# OUTPUT 
# Attach a statement for to the number in range.
print("The number in range for the numbers you entered is "+ str(randomnumb1) + ".")
print(randomnumb1)