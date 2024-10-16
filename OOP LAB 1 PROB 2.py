#************************************************************************************************
# Lab Exercise #1: Problem No. 2 
# Programmed by: Ahiezer Dayl P. Dalangin
# Course, Year and Section: BSCpE 1-3
# Instructor: Engr. Julius S. Cansino
# Date Submitted: March 10, 2024
#************************************************************************************************

print ("Program Title: Lab Exercise #1 | Problem No. 2")
print ("Programmed by: Ahiezer Dayl P. Dalangin")

print ("Decryption Guide: \n a=* \n e=& \n i=# \n o=+ \n u=!")

# Input a statement to encrypt
text = input("\nEnter the text to encrypt: ")

# Convert the special character to its own assign letter
decrypted_text = text.replace('*', 'a').replace('&', 'e').replace('#', 'i').replace('+', 'o').replace('!', 'u')

print("\nDecrypted text:", decrypted_text)

# End of Program





