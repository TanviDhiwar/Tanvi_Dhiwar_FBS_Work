#swap two numbers without using third variable
a = int(input("Enter number1:"))
b = int(input("Enter number2:"))

print(f"before swapping a:",a,"b:",b)
a , b = b , a

print("after swapping:a:",a,"b:",b)