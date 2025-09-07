correct_userid = "tanvi"
correct_password = "1234"

for attempt in range(3+1):
    userid = input("Enter User ID: ")
    password = input("Enter Password: ")

    if userid == correct_userid and password == correct_password:
        print("Login successful!")
        break
    else:
        print("Incorrect User ID or Password.!Try Again")

else:
     print("Maximum attempts reached. Access denied.")
