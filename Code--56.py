char = input("Enter an alphabet character: ")
lower_char = char.lower()
if lower_char in ['a', 'e', 'i', 'o', 'u']:
 print(char, "is a Vowel")
elif lower_char.isalpha():
 print(char, "is a Consonant")
else:
 print("Invalid input! Please enter an alphabet.")
