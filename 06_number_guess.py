import random
number = random.randint(1, 10)
random_number = number
guess_amount = 1
code_exit = False

while guess_amount != 4 and code_exit == False:
    guess = int(input("Guess a number between 1 and 10\n"))
    if guess != random_number:
        print("Incorrect")
        guess_amount = guess_amount + 1
    elif guess == random_number:
        print("Correct")
        code_exit = True

if guess_amount == 4 and guess != random_number:
    print("You have run out of guesses the number was {}".format(random_number))

elif guess == number:
    print("Good job you guessed the number in {} guess/es".format(guess_amount))
