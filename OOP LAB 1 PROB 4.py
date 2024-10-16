# Lab Exercise #1: Problem No. 4
# Programmed by: Ahiezer Dayl P. Dalangin
# Course, Year and Section: BSCpE 1-3
# Instructor: Engr. Julius S. Cansino
# Date Submitted: March 10, 2024

#************************************************************************************************#


# Input a statement
text = input("Enter a statement: ")

# Assign letters according to its own category
vowels = "aeiouAEIOU"
consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
digits = "0123456789"

# Assign a variable for counting
vowel_count = 0
consonant_count = 0
digit_count = 0
special_count = 0

# Formula for counting the characters or digits
for char in text:
    if char in vowels:
        vowel_count += 1
    elif char in consonants:
        consonant_count += 1
    elif char in digits:
        digit_count += 1
    else:
        special_count += 1

characters = vowel_count + consonant_count + digit_count + special_count

print("\nNumber of vowels:", vowel_count)
print("Number of consonants:", consonant_count)
print("Numbers of digits:", digit_count)
print("Number of special characters (including spaces):", special_count)
print("Total number of characters found in the string:", characters)

# End of program



