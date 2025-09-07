#Fibonacci series
no = int(input("Enter a no:"))
a = 0
b = 1
print("Fibonacci series:")
for i in range(no):
    print(a, end =" ")
    a,b = b, a + b