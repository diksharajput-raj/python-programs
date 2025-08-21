A = int(input("Enter a number: "))
rev = 0
temp = A
while temp > 0:
    rev = rev * 10 + temp % 10
    temp //= 10
if A == rev:
    print("Yes")
else:
    print("No")
