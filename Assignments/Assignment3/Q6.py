#WAP to calculate profit or loss
cp = float(input("Enter Cost Price:"))
sp = float(input("Enter Selling Price:"))

if(sp > cp):
    profit = sp - cp
    print("profit:",profit)
elif(cp > sp):
    loss = cp - sp
    print("Loss:",loss)
else:
    print("NO PROFIT NO LOSS")
