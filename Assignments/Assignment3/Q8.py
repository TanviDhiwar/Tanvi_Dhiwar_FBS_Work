#captcha verification after login
import random

userid = "tanvi"
password = "tanvi25"

u = input("Enter userid: ")
p = input("Enter password: ")

if u == userid and p == password:
    captcha = random.randint(1000, 9999)
    print("Captcha:", captcha)
    user_captcha = int(input("Enter the captcha: "))

    if user_captcha == captcha:
        print("Login Successful")
    else:
        print("Login Failed (Captcha mismatch)")
else:
    print("Invalid userid or password")