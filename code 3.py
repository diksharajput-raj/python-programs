# Take input from user
num = int(input("Enter a number: "))

# Check if divisible by 3 AND last digit is 4
if num % 3 == 0 and num % 10 == 4:
    print("The number is divisible by 3 and the last digit is 4.")
else:
    print("Condition not satisfied.")