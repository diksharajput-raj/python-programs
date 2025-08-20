#Take input from user
num = int(input("Enter a number: "))

# Check if divisible by 7 OR last digit is 5
if num % 7 == 0 or num % 10 == 5:
    print("The number is divisible by 7 or the last digit is 5.")
else:
    print("Condition not satisfied.")