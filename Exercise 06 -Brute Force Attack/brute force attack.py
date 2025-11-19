# Password brute force simulation

correct_password = "12345"
attempts = 5

while attempts > 0:
    user_input = input("Enter the password: ")

    if user_input == correct_password:
        print("Access granted.")
        break
    else:
        attempts -= 1
        if attempts > 0:
            print("Wrong password. Attempts left:", attempts)
        else:
            print("Too many wrong attempts. Authorities have been alerted.")
