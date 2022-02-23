# Checks they inputted viable answer

question_check = False

# Asks user for input on vegetable

while not question_check:
    vegetable_guess = input("Pick either Carrot, Broccoli, Peas or Sweetcorn I will attempt to guess your choice.\n").lower().strip()

    if vegetable_guess == "carrot" or vegetable_guess == "broccoli" or vegetable_guess == "peas" or vegetable_guess == "sweetcorn":
        question_check = True
    else:
        print("Please input a valid answer\n")

# Asks user question 1
question_check = False

while not question_check:
    question_1 = input("Is the vegetable green? Y/N \n").lower().strip()

    if question_1 == "y" or question_1 == "n":
        question_check = True

    else:
        print("Please input valid answer\n")

# Asks user question 2
question_check = False

if question_1 == "n":
    while not question_check:
        question_2 = input("Is the vegetable orange? Y/N \n").lower().strip()

        if question_2 == "y" or question_2 == "n":
            question_check = True
        else:
            print("Please input valid answer\n")

# Asks user question 3
question_check = False

if question_1 == "y":
    while not question_check:
        question_3 = input("Does your vegetable look like a tree? Y/N \n").lower().strip()

        if question_3 == "y" or question_3 == "n":
            question_check = True
        else:
            print("Please input valid answer\n")

# Asks user question 4
question_check = False

if question_1 == "n" and question_2 == "n":
    while not question_check:
        question_4 = input("Is the vegetable yellow? Y/N \n").lower().strip()

        if question_4 == "y" or question_4 == "n":
            question_check = True
        else:
            print("Please input valid answer\n")

if question_1 == "n" and question_2 == "y":
    vegetable = "carrot"
elif question_1 == "y" and question_3 == "y":
    vegetable = "broccoli"
elif question_1 == "y" and question_3 == "n":
    vegetable = "peas"
elif question_1 == "n" and question_2 == "n" and question_4 == "y":
    vegetable = "sweetcorn"

if vegetable == vegetable_guess:
    print("Your vegetable is {} I got it right!".format(vegetable))
elif vegetable != vegetable_guess:
    print("I feel as though you've cheated")
else:
    print("You've beaten me")
