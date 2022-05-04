"""
Author: Cordelia Thomas
Date Created: April 29, 2022
Course:ITT103
Purpose: This program is to calulate the commission of an undetermined number of sales persons basedon their sales amount and their sales class.
"""


# The program terminator will determine how many times the codes are exectuted.

program_terminator = 'yes'

# The while loop will allow the program to be repeated once the condition is true.
while program_terminator != 'no' :

# INPUT
# The user will be prompted to input the necessary data. 
# Once the try block raises an error, the except block will be executed.
# If a value error is detected, the user will be asked to enter a valid number.
  try:
    salesperson_no = int(input("Please enter sales person number "))
  except ValueError:
    print("Invalid input. Please enter a valid number")
    salesperson_no = int(input("Please enter sales person number ")) 
  try:
    sales_amt = float(input("Please enter your sales amount "))
  except ValueError:
    print("Invalid input. Please enter a valid amount")
    sales_amt = float(input("Please enter your sales amount "))
  try:
    sales_class = int(input("Please enter sales class "))
  except ValueError:
    print("Invalid input. Please enter a valid number")
    sales_class = int(input("Please enter sales class "))

# An error message will be printed once the user enters a sales class value greater than 3 or equals 0.
  if sales_class > 3 or sales_class == 0:
    print("Invalid sales class. Please re-enter a number from one to three.")
    sales_class = int(input("Please enter sales class ")) # User is prompted to re-enter a valid number. 

# IF-STATEMENT CALCULATIONS
# commission calculations when class entered is 1
  if sales_class == 1:
    if sales_amt <= 1000:
      commission = sales_amt * 0.06
    elif sales_amt > 1000 and sales_amt < 2000:
      commission = sales_amt * 0.07
    else:
      commission = sales_amt * 0.1
      
# commission calculations when class entered is 2   
  if sales_class == 2:
    if sales_amt <= 1000:
      commission = sales_amt * 0.04
    else:
      commission = sales_amt * 0.06

# commission calculation when class entered is 3
  if sales_class == 3:
    commission = sales_amt * 0.045

# OUTPUT
# This will be displayed to the user once the calculations are done.
  print("Employee Sales Number:",salesperson_no)
  print("Total Sales Amount: $",sales_amt)
  print("Employee Sales Class:", sales_class)
  print("Total Commission: $",(round(commission, 2)))

# The user will be prompted to continue or exit the program.
# Once the user opt to continue, the program will ask the user to make another entry.
  program_terminator = input("Do you want to make another entry? Write yes to continue and no to exit ")
  
else:
    print("Goodbye!") # The user types no and exits the program.
