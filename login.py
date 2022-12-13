from time import sleep  
username = "mina"
password = "secretpassword"

username_input = input("Username: ")
password_input = input("Password: ")

if username_input == username and password_input == password:
    print("Access Granted")
    print("Please wait....")
    sleep(3)
    print("Ok... loading...")
    sleep(1)
    print("...")
    sleep(1)
    print("...")
    sleep(1)
    print("Ok you have security clearance. Pulling up the secret mainframe")
elif username_input == username and password_input != password:
    print("Password Incorrect")
elif username_input != username and password_input == password:
    print("Username incorrect")
else:
    print("You might wanna check...")