

x = int(input("Enter first angle: "))
y = int(input("Enter second angle: "))
z = int(input("Enter third angle: "))
if x + y + z == 180:
    if x == 90 or y == 90 or z == 90:
        print("Right Triangle")
    elif x > 90 or y > 90 or z > 90:
        print("Obtuse Triangle")
    else:
        print("Acute Triangle")
else:
    print("Not a valid triangle")
