#prime or not
no = int(input("enter a no:"))
for i in range(2,no):
    if(no % i == 0):
        print(f"{no} is not a prime number.")
        break

else:
    print(f"{no} is prime number.")
