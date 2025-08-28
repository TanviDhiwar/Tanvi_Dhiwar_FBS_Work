a = float(input('Enter value of a:'))
b = float(input('Enter value of b:'))
c = float(input('Enter value of c:'))

d=(b *b) - (4*a*c)

root1 = (-b+ d ** 0.5)/(2*a)
root2 = (-b- d ** 0.5)/(2*a)

print(f'Root1 is{root1}')
print(f'Root 2 is{root2}')