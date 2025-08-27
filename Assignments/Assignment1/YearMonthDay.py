days = int(input('Enter Days:'))

year = days // 365
days = days % 365
week = days // 7
days = days % 7

print(f'Total Years:{year}')
print(f'weeks:{week}')
print(f'days:{days}')