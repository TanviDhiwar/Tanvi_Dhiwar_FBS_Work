p1 = int(input("Enter a price of product 1:"))
p2 = int(input("Enter a price of product 2:"))
p3 = int(input("Enter a price of product 3:"))
p4 = int(input("Enter a price of product 4:"))
p5 = int(input("Enter a price of product 5:"))

total = p1 + p2 + p3 + p4 + p5
if(total > 0):
    gst = total * 0.18
    final = total + gst
    print("subtotal:",total)
    print("GST 18%:",gst)
    print("Total Bill:",final)
else:
    print("NO PRODUCT PURCHASE")