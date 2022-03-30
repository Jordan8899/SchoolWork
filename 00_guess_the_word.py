stored_pass = "sandwich"
password = ""
pass_mismatch = stored_pass != password
attempts = 5

password_letters = len(stored_pass)
first_letter = stored_pass[0]
amount = password_letters - 1
last_letter = stored_pass[amount]

print("The password has {} letters".format(password_letters))

while attempts > 0:
    print("Enter your password:")
    password = input()

    if password != stored_pass:
        attempts = attempts - 1

        if attempts == 4:
            print("The first letter is {}".format(first_letter))
        elif attempts == 2:
            print("The last letter is {}".format(last_letter))

    else:
        break

if password == stored_pass:
    print("Congrats, you win!")
else:
    print("Incorrect, you lose!")
