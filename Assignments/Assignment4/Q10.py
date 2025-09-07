# perfect number or not
n = int(input("Enter a number: "))
sum_div = 0
for i in range(1, n):
    if n % i == 0:
        sum_div += i

if sum_div == n:
    print(f"{n} is a Perfect Number")
else:
    print(f"{n} is NOT a Perfect Number")