#*******************************************************************************
#Lab Assignment #4 Problem 3
#Programmed by: Dalangin, Ahiezer Dayl P.
#Course, Year, and Section: BSCpE 1-3
#Instructor: Engineer Julius S. Cansino
#Date of Submission: April 21, 2024
#*******************************************************************************
print ("Program Title: Lab Assignment 4 Problem 3")
print ("Programmed by: Ahiezer Dayl P. Dalangin") 

#Program an interactive calculator

#Create a class for the formula error
class FormulaError(Exception):
    pass

while True:
    try:
#Input the equation
        formula=input("\nPlease enter an equation with 2 numbers and an operator (i.e 1 + 1): ")
        
#Split the input
        split = formula.split()
        
#Prompt for error in entering 3 values
        if len(split) != 3:
            raise FormulaError("ERROR! Please enter 2 numbers and an operator separated by spaces ")
            
#Formula for operators
        num1, operator, num2 = split
        num1 = float(num1)
        num2 = float(num2)
        if operator not in ['+', '-']:
            raise FormulaError("ERROR. Please use '+' or '-' only. ")
        if operator == '+':
            result = num1 + num2
        else:
            result = num1 - num2
        print("Result= ", result)
        
#Prompt for value and formula errors
    except (FormulaError, ValueError) as FE:
        print(FE)

#Prompt for re-trial    
    retry = input("\nDo you want try again? Answer 'yes' if so, and asnwer 'quit' if you don't want to: " )
    if retry.lower() == "yes":
        continue
    elif retry.lower() == "quit":
        print("Program has ended")
        break
    else:
        break
    
#End of program
        
        
