#************************************************************************************************
# Lab Exercise #1: Problem No. 3 
# Programmed by: Ahiezer Dayl P. Dalangin
# Course, Year and Section: BSCpE 1-3
# Instructor: Engr. Julius S. Cansino
# Date Submitted: March 10, 2024
#************************************************************************************************

print ("Program Title: Lab Exercise #1 | Problem No. 3")
print ("Programmed by: Ahiezer Dayl P. Dalangin")

# Get user input
text = input("\nEnter the message (all uppercase letters, no spaces): ")
keyword = input("Enter the keyword (all uppercase letters, no spaces): ")
# Convert plaintext and keyword to uppercase
text = text.upper()
keyword = keyword.upper()

# Generate the Vigenère square
vigenere_square = [[(i + j) % 26 for j in range(26)] for i in range(26)]

# Encrypt the message
ciphertext = ""
add_values = ""
mod_values = ""
for i in range(len(text)):
    # Convert letters to corresponding number values (A=0, B=1, ..., Z=25)
    j = ord(text[i]) - 65
    k = ord(keyword[i % len(keyword)]) - 65
    # Add the values from the Vigenère square and take the result mod 26
    l = (vigenere_square[j][k] + 65)
    # Append the encrypted character to the ciphertext
    ciphertext += chr(l)
    # Record add and mod values
    add_values += str(vigenere_square[j][k]) + " "
    mod_values += str((vigenere_square[j][k] + 65) % 26) + " "

print("Add: ", add_values)
print("Mod: ", mod_values)
print("\nCiphertext:", ciphertext)
