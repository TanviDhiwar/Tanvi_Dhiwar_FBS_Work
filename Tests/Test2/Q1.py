#Leap Year Flow Chart
year = int(input("Enter year:"))

if(year % 4 == 0):
    if(year % 100 == 0):
        if(year % 400 == 0):
            print(f"{year}:LEAP YEAR")
        else:
            print(f"{year}:NOT a LEAP YEAR..")
    else:
        print(f"{year}:leap year..")
else:
    print(f"{year}:NOT a Leap Year") 