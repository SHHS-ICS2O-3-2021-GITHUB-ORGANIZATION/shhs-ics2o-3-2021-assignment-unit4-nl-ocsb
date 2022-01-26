# NAME OF AUTHOR: Nyandea Lansana
# NAME OF THE PROGRAM: Prime Numbers
# DATE OF CREATION: Jan. 24, 2022
# PURPOSE OF PROGRAM: To a program that tells the user the prime numbers based on the numbers entered. 

import time
# Program Title
print ("Prime Numbers Calculator")

time.sleep(1)
# some information about what are prime numbers 
# and how to use the program
print("\nWhat are prime numbers, and what do they mean? Prime numbers are positive integers bigger than one that have only one and the number itself as factors. This tool allows you to enter two numbers and displays the prime numbers that lie between them. It will first ask you to provide a lower bound, which implies the first number you enter. Furthermore, it prompts you to input an upper bound, which is the second number you want to use. The computer will then tell you the prime numbers that lie between the numbers you specified.")

print("\nNow go ahead and try it out by following the directions.")

# VARIABLE DEFINITION 
firstnumber = 0
secondnumber = 0 

# INPUT

# taking input for the two numbers so it the program 
# can output prime numbers between two numbers
firstnumber = int(input("\nEnter in an integer for a lower bound:"))
secondnumber = int(input("Enter in an integer for an upperbound:"))

time.sleep(1)

#PROCESSING & OUTPUT
print("\nPrime numbers between", firstnumber, "and", secondnumber, "are:")

# +1 because all prime numbers are greater than one
for answer in range(firstnumber, secondnumber + 1):
   if answer > 1:
      # the range starts from 2 because it's the start of
      # prime numbers and it is also greater than one

       for i in range(2, answer):
          # to check if number is divisible or not

           if answer % i == 0:
               break
       else:
           print(answer)