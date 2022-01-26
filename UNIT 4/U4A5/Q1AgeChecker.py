# NAME OF AUTHOR: Nyandea Lansana
# NAME OF THE PROGRAM: Age Checker
# DATE OF CREATION: Jan. 24, 2022
# PURPOSE OF PROGRAM: To tell the user whether they're in elementary, intermediate, highschool, or univesity/college/workforce based on their age entered. 

# Program Title
print ("Age Checker")
print ()

# VARIABLE DEFINITION
# initializing the user's age
age = 0

# INPUT
# tell the user what this program can do
print("Hello, this age checker can tell whether you're in elementary, intermediate, highschool, or university/college/workforce. Try it out an see! ")

# initializing user's age to an input function
age = int(input("\nPlease enter your age:"))


# PROCESSING & OUTPUT
# Use a while loop with comparison operator for the age ranges 
while True:
    # condition statement for the user's age 
    # initializing print statement based on 
    # what the user entered
    if age < 5:
      print("You have not started school yet.")
      break
    if age <= 11: 
        print("You're in elementaty school.")
        break
    if age <= 14:
        print("You're an intermediate.")
        break
    if age <= 18:
        print("You're in highschool.")
        break
    if age >= 19:
        print("You're either in university, college or the workforce.")
        break