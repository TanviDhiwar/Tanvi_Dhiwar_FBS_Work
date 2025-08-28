a = int(input("Enter Side1:"))
b = int(input("Enter Side2:"))
c = int(input("Enter Side3:"))

if(a == b == c):
    print("Equilateral Triangle")      #if all three sides are equals
elif(a == b or b == c or c == a):
    print("Isosceles Triangle")        #if two sides are equal
else:
    print("Scalene Triangle")          #otherwise  