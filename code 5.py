# Take input from user
A = int(input("Enter a number: "))

# Check if divisible by both 5 and 11
if A % 5 == 0 and A % 11 == 0:
    print("The number is divisible by both 5 and 11.")
else:
    print("The number is NOT divisible by both 5 and 11.")