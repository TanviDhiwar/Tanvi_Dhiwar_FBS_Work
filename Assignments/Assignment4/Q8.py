#WAP to find which numbers are divisible by 7 and multiple of 5 in a given range . 
start = int(input("Enter Start:"))
end = int(input("Enter End:"))
print("Number is divisible by 7 and multiple of 5 are:")
for i in range(start, end + 1):
    if(i % 7 == 0 and i % 5 == 0):
        print(i,end = " ")