no = int(input("Enter number of student"))

total_perc = 0

for i in range(1,no + 1):
    marks = 0
    print(f"Enter marks of 5 subjects for student {i}:")
    for j in range(5):
        marks += int(input(f"subject {j+1}:"))

    percentage = marks / 5
    print(f"percentage of student {i} = {percentage}")
    total_perc += percentage

avg = total_perc / no
print("average percentage of all students =",avg)