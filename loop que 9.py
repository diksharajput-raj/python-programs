N = int(input("Enter a number: "))
s = 0
temp = N
while temp > 0:
    s += temp % 10
    temp //= 10
print(s)
