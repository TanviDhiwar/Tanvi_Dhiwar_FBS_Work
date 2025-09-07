#factorial of Number
no = int(input("Enter a Number:"))
fact = 1
for i in range(1 ,no + 1):
    fact *= i
print(f"Factorial of {no} is:{fact}")
