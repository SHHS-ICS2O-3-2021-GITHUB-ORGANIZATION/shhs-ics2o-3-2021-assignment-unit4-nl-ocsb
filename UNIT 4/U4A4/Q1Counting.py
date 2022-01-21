# NAME OF AUTHOR: Nyandea Lansana
# NAME OF THE PROGRAM: Counting Program
# DATE OF CREATION: Jan. 19, 2022
# PURPOSE OF PROGRAM: To count to a number and count down by a desired number. 

# Program Title
print ("Counting Program")
print ()

# Importing a time module
import time

# VARIABLE DEFINITION
current_count = 0
countby = 0

# INPUT
# Assign variables to an input function
large_number = int(input("What large number do you want to count to? Please enter an integer: "))
countby = int(input("What number do you want to count by? Please enter an integer: "))

# PROCESSING
# Use while loop; count up from 1 to number inputted 
# Use while loop; countdown by the number entered
# sleep function so it executes program one at a time
# else and elif statement 
# code for if number entered not a perfect countdown
# for eg. if large number is 9; countby is 5, don't want it to count to ten. should stop at nine. 
print(current_count)
while True:
    time.sleep(1)
    current_count = current_count + countby
    if current_count == large_number:
      print(current_count)
      break
    elif current_count < large_number:
      print(current_count)
    else:
      # current_count > large_number
      # don't want it to greater than the number entered
      # so stop at number entered
      current_count = large_number
      print(current_count)
      break
while True:
  time.sleep(1)
  current_count = current_count - countby
  if current_count == large_number:
    print(current_count)
    break
  elif current_count > 0:
    print(current_count)
  else:
    print(0)
    break

# OUTPUT
# Display the end of the timer to the user.
print('Blast Off!')