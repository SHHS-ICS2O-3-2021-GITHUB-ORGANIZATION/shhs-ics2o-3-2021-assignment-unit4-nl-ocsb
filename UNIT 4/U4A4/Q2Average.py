# NAME OF AUTHOR: Nyandea Lansana
# NAME OF THE PROGRAM: Sum and Average Calculator 
# DATE OF CREATION: Jan. 19, 2022
# PURPOSE OF PROGRAM: To create a program that display sum and average based on the value numbers entered

# Program Title
print ("Sum and Average Calculator")
print ()

# VARIABLE DEFINITION

count = 0
total = 0

# INPUT
# Read the first value entered and increase count of how many values were entered 
value = float(input("Please enter a number and input 0 when you're finished: "))
while value!= 0:
  total = total + value 
  count = count + 1

# Read for the next value
  value = float(input("Please enter another number: "))

# PROCESSING
# If statement for when value entered is 0
# An error prompt if the user just entered 0
if count == 0:
  print("No valid numbers where entered.")
  

# OUTPUT
# Else statement for when the value is isn't 0
# Adds sum and divide by the count 
else:
  average = total / count
  print("The average of what you entered is ", average)
  print("The sum of what you entered is ", total)