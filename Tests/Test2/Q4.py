l = int(input("Enter Length:"))
b = int(input("Enter Breadth:"))
h = int(input("Enter height:"))
rate = int(input("Enter a cost:"))

area = 2 * (l + b) * h
total_cost = area * rate

print(f"Total wall area:{area}sqm")
print(f"Total Painting cost: rs{total_cost}")