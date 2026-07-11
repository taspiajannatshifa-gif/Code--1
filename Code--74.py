print("Printing 1 to 10 except the number 5:")
for i in range(1, 11):
 if i == 5:
 continue # Skips the rest of the loop block for i = 5
 print(i, end=" ")
