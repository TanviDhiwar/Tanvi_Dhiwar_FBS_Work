area = int(input('Enter Area of wall:'))
interior = int(input('Enter cost of interior painting:'))
Exterior = int(input('Enter cost of Exterior painting:'))

total_area = 7 * area
Interior = total_area * interior
Exterior = total_area * Exterior

print(f'interior wall:{Interior}')
print(f'Exterior wall:{Exterior}')