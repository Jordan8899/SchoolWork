# Variables
import random
number = random.randint(1, 10)
guess_amount = 1
code_exit = False

# Main Routine
while guess_amount != 4 and not code_exit:
    try:
        guess = int(input("Guess a number between 1 and 10\n"))

        if guess != number:
            guess_amount = guess_amount + 1

            if guess > number:
                print("Incorrect, it's lower\n")
            elif guess < number:
                print("Incorrect, it's higher\n")

        elif guess == number:
            print("Correct\n")
            code_exit = True

        else:
            print("Please input int")
    except ValueError:
        print("Please input int")

if guess_amount == 4 and guess != number:
    print("You have run out of guesses the number was {}".format(number))

elif guess == number:
    print("Good job you guessed the number in {} guess/es".format(guess_amount))
