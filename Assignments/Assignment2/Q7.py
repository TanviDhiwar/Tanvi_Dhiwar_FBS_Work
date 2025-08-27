#sum of three digits
num = int(input("Enter Any Three Digits Numbers:"))

d1 = num % 10
num = num // 10

d2 = num % 10
num = num // 10

d3 = num % 10
num = num //10

print(f'sum of digit : d1:{d1},d2:{d2},d3:{d3} is = {d1 + d2 + d3}')
