# NAME OF AUTHOR: Nyandea Lansana
# NAME OF THE PROGRAM: Total Cost Of Items With Taxes
# DATE OF CREATION: Jan. 12, 2022
# PURPOSE OF PROGRAM: To help the user calculate the total cost of items, the taxes and the total cost of the users' item with taxes. 


# VARIABLE DEFINITION

item1 = 0
item2 = 0
item3 = 0
item4 = 0
item5 = 0
item6 = 0
item7 = 0
item8 = 0
item9 = 0
item10 = 0
totalcostofitems =  0
taxes = 0
totalcostofitemsandtaxes = 0

# INPUT

name = input('Please enter your name: ')
print('Hello ' + name)
print(input(name + ', please follow the prompts and enter your items! '))

item1 = int(input("Please enter the cost of the first item:"))
item2 = int(input("Please enter the cost of the second item:"))
item3 = int(input("Please enterthe cost of the third item:"))
item4 = int(input("Please enter the cost of the fourth item:"))
item5 = int(input("Please enter the cost of the fifth item:"))
item6 = int(input("Please enter the cost of the sixth item:"))
item7 = int(input("Please enter the cost of the seventh item:"))
item8 = int(input("Please enter the cost of the eigth item:"))
item9 = int(input("Please enter the cost of the ninth item:"))
item10 = int(input("Please enter the cost of the tenth item:"))

# PROCESSING

totalcostofitems = (item1 + item2 + item3 + item4 + item5 + item6 + item7 + item8 + item9 + item10)
taxes = totalcostofitems * 0.13
totalcostofitemsandtaxes = taxes + totalcostofitems

# OUTPUT

print("The taxes of this items is: " + "$" + str(taxes))
print("The cost of the total items without taxes is: " + "$" + str(totalcostofitems)) 
print("The cost of total items with taxes: " + "$" + str (totalcostofitemsandtaxes))
print(input('Thanks ' + name + ', for using this calculator. Have a good day!'))