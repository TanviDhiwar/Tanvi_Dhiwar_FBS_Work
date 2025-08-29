#total cost of fencing the field
#given values
radius = 20
length = 50
breadth = 40
cost_per_meter = 35

circle_part = radius ** 0.5
rectangle = length + breadth + radius

total_perimeter = circle_part + rectangle

total_length = total_perimeter * 5

total_cost = total_length * cost_per_meter

if(total_cost > 0):
    print(f"total cost of fencing the field :{total_cost}Rs.")
else:
    print("Invalid Calculation")