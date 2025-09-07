#WAP to print all numbers in a range divisible by a given number.

start = int(input("Enter Start:"))
end = int(input("Enter End:"))
divisior = int(input("Enter Divisior:"))

print(f"Number divisible by {divisior}")
for i in range(start , end + 1):
    if(i % divisior == 0):
        print(i, end =" ")