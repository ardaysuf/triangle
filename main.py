a = int(input("Enter the First Length of Side: "))
b = int(input("Enter the Second Length of Side: "))
r = int(input("Enter the Third Length of Run: "))

if (a + b < r or abs(a - b) > r):
    print("Invalid Values...")
    quit()
elif (b + r < a or abs(b - r) > a):
    print("Invalid Values...")
    quit()
elif (a + r < b or abs(a - r) > b):
    print("Invalid Values...")
    quit()        
else:
    if (a == b  and b != r):
        print("Isosceles Triangle")
    elif (a == b and b == r):
        print("Equilateral Triangle")
    else:
        print("Scalene Triangle")       

perimeter = a + b + r

h = int(input("Enter the Lenght of Height: "))

area = (r * h) / 2

print("Perimeter of the Triangle = " + str(perimeter))
print("Area of the Triangle = " + str(area))

