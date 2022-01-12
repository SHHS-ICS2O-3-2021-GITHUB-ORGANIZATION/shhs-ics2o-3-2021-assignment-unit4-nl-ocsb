# NAME OF AUTHOR: Nyandea Lansana
# NAME OF THE PROGRAM: Volume Of A Rectangular Prism
# DATE OF CREATION: Jan. 12, 2022
# PURPOSE OF PROGRAM: To aid the user in calculating the volume of a rectangular prism.  


# VARIABLE DEFINITION

length = 0
width = 0
depth = 0


# INPUT

length = int(input("Please enter a value for the length:"))
width = int(input("Please enter a value for the width:"))
depth = int(input("Please enter a value for the depth:"))

# PROCESSING

volume = (length * width * depth)

#OUTPUT

print("The volume of the rectangular prism is: " + str(volume))