#swap two numbers using third variable
no1 = int(input("Enter Number1:"))
no2 = int(input("Enter Number2:"))

print(f"Before Swapping no1=",no1, "no2=",no2)

c = no1
no1 = no2
no2 = c

print(f"After Swapping no1=",no1, "no2=",no2)