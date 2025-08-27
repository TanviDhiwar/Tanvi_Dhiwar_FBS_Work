sub1 = int(input("Enter Marks of SUbject1:"))
sub2 = int(input("Enter Marks of SUbject2:"))
sub3 = int(input("Enter Marks of SUbject3:"))
sub4 = int(input("Enter Marks of SUbject4:"))
sub5 = int(input("Enter Marks of SUbject5:"))

gain_marks = sub1 + sub2 + sub3 + sub4 + sub5
per = (gain_marks / 500)*100

print(f"Total percentage{per}%.")

if(per >= 90):
    print("First Class")
elif(per >= 70):
    print("Second Class")
elif(per >= 50):
    print("Third Class")
elif(per >= 35):
    print("PASS")
else:
    print("FAIL")


