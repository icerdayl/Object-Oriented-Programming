#*******************************************************************************
#Lab Assignment #4 Problem 1
#Programmed by: Dalangin, Ahiezer Dayl P.
#Course, Year, and Section: BSCpE 1-3
#Instructor: Engineer Julius S. Cansino
#Date of Submission: April 21, 2024
#*******************************************************************************
print ("Program Title: Lab Assignment 4 Problem 1")
print ("Programmed by: Ahiezer Dayl P. Dalangin")
#Make a program that inputs a number and calculate its square root. Negative numbers are not allowed.

#Import a math module
import math

#Input the number and determine if it is a positive
try:
    num = int(input("Enter a number: "))
    if num < 0:
        raise ValueError("INVALID! The number cannot be calculated since it's a negative number.")
        
#Get the square root of the number
    SquareRoot = math.sqrt(num)
    print("Square root: ", SquareRoot)
    
#Append or Write the number to the text file    
    with open("sqrt_results.txt", "a") as file:
        file.write(f"Number: {num}, Square Root: {SquareRoot}")
        
#Prompt for value error
except ValueError as error:
    print(f"Error: {error}")
    
#End of Program