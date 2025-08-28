#palindrome or not
no = int(input("Enter Three Digits Number:"))

d1 = no // 100
d2 = (no // 10) % 10
d3 = no % 10

rev = d3 * 100 + d2 * 10 + d1

if(no == rev):
    print(f"{no} is palindrome number")
else:
    print(f"{no} is not palindrome number")