#*******************************************************************************
#Lab Assignment #4 Problem 2
#Programmed by: Dalangin, Ahiezer Dayl P.
#Course, Year, and Section: BSCpE 1-3
#Instructor: Engineer Julius S. Cansino
#Date of Submission: April 21, 2024
#*******************************************************************************
print ("Program Title: Lab Assignment 4 Problem 2")
print ("Programmed by: Ahiezer Dayl P. Dalangin")
#Write a program that reads a text file wile using exception handling functions

#Input a file name
name= input("Please enter your desired file name: ")

#Open and read the text file's contents
try:
    file=open(name, 'r')
    contents = file.read()
    print("File contents:", contents)

#Prompt for errors        
except (FileNotFoundError, IOError) as FE:
    print (FE)

#Prompt for finally block    
finally:
    print ("Program has ended")

#End of Program