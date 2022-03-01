def value_checker(value):
    valid = False
    while not valid:
        try:
            response = int(input(value))
            return response

        except ValueError:
            print("Error please enter a whole number\n")


def highest(a, b):
    if a > b:
        highest_number = a

    elif b > a:
        highest_number = b

    print("The highest number inputted is", highest_number)

num1 = value_checker("Choose a number ")
num2 = value_checker("Choose a 2nd number ")

highest(num1, num2)
