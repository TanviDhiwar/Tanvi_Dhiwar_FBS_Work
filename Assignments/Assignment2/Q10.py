#revese number
num = int(input("Enter any three digits of number:"))

no1 = num % 10
num = num // 10

no2 = num % 10
num = num // 10

no3 = num % 10
num = num //10

print(f"Reverse number of given number is: no1:{no1},no2:{no2},no3:{no3}")