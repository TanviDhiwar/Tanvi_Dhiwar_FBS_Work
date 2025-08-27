#Total salary of employee
basic = int(input("Enter Basic Salary"))

da = 0.10 * basic      #Dearness Allowance 
ta = 0.12 * basic      #Travel Allowance
hra = 0.15 * basic     #House Rent Allowance

total_salary = da + ta + hra

print(f"basic salary:{basic}")
print(f"Dearness Allowance:{da}")
print(f"Travel Allowance:{ta}")
print(f"House Rent Allowance:{hra}")
print(f"total salary of employee:{total_salary}")