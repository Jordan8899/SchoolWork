stored_pass = "sandwich"
password = ""
pass_mismatch = stored_pass != password
attempts = 5
count_e = 0

password_letters = len(stored_pass)
first_letter = stored_pass[0]
amount = password_letters - 1
last_letter = stored_pass[amount]

print("The password has {} letters\n".format(password_letters))
user_letter = input("What letter would you like to test for? ")

for letter in stored_pass:
    if letter == user_letter:
        count_e = count_e + 1

print("{} appears {} in the word".format(user_letter, count_e))

while attempts > 0:
    print("\nEnter your guess:")
    password = input().strip().lower()

    if password != stored_pass:
        attempts = attempts - 1

        if attempts == 4:
            print("\nThe first letter is {}".format(first_letter))
        elif attempts == 2:
            print("\nThe last letter is {}".format(last_letter))

    else:
        break

if password == stored_pass:
    print("\nCongrats, you win!")
else:
    print("\nIncorrect, you lose!")
