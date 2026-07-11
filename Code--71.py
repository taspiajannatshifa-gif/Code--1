num = int(input("Enter a number: "))
temp = abs(num)
sum_digits = 0
while temp > 0:
 digit = temp % 10
 sum_digits += digit
 temp = temp // 10
print("Sum of digits is:", sum_digits)
