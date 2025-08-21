l = int(input('Enter the length:'))
b = int(input('Enter the breadth:'))
r = int(input('Enter the Radius:'))

area = (l * b) + (1/2 * 3.14 * r * r)
peri = (2 * b) + l + (3.14 * r)

print(f'Area of figure:{area}')
print(f'Perimeter of figure:{peri}')