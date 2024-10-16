#*******************************************************************************
#Lab Assignment #3 
#Programmed by: Dalangin, Ahiezer Dayl P.
#Course, Year, and Section: BSCpE 1-3
#Instructor: Engineer Julius S. Cansino
#Date of Submission: April 6, 2024
#*******************************************************************************
print ("Program Title: Lab Assignment #3")
print ("Programmed by: Ahiezer Dayl P. Dalangin")

#Write a program making a simple calculator solving 2 sets of numbers
#Defining the operators
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Number cannot be divided by zero.")
    return x / y
    
#Prompt for solving 
def solve(operation, x, y):
    if operation == 'addition':
        return add(x, y)
    elif operation == 'subtraction':
        return subtract(x, y)
    elif operation == 'multiplication':
        return multiply(x, y)
    elif operation == 'division':
        return divide(x, y)
    else:
        raise ValueError("Invalid operation!")

#Input the numbers
def main():
    while True:
        try:
            operation = input("\nChoose an operation (Addition, Subtraction, Multiplication, Division): ").lower()
            if operation not in ['addition', 'subtraction', 'multiplication', 'division']:
                raise ValueError("Invalid operation!")
            
            x = float(input("Enter the first number: "))
            y = float(input("Enter the second number: "))

#Error trapping            
            result = solve(operation, x, y)
            print("Result:", result)
        except ValueError as X:
            print("Error:", X)
            continue
#Prompt for re-trial       
        retry = input("Do you want to try again? (yes/no): ").lower()
        if retry != 'yes':
            print ("Thank You!")
            break
        else:
            continue
main()
#End of Program

