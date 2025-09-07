#WAP to print all integers upto n that aren't divisible by 2 and 3.
no = int(input("Enter a Number:"))
print("Number is Not divisible by 2 and 3 are:")
for i in range(1, no + 1):
    if(i % 2 != 0 and i % 3 != 0):
        print(i,end = " ")