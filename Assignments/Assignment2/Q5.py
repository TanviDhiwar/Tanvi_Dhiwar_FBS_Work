cost_price = int(input("Enter cost price:"))
discount = int(input("Enter discount:"))

discount = (discount / 100) * cost_price
selling_price = cost_price - discount

print(f"Selling Price of book is:{selling_price}")

