p = int(input('Enter principle Amount:'))
r = int(input('Enter Rate of intrest per year:'))
t = int(input('Enter time:'))

CI = p * (1 + r/100)**t - p

print(f'Compound Intrest is {CI}')