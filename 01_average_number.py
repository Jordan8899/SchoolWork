def value_checker(value):
    valid = False
    while not valid:
        try:
            response = int(input(value))
            return response

        except ValueError:
            print("Error please enter a whole number\n")


def average_value(a, b, c):
    average = a + b + c
    average = average / 3
    print("The average is {}".format(average))

num1 = value_checker("Choose a number ")
num2 = value_checker("Choose a 2nd number ")
num3 = value_checker("Choose a 3rd number ")

average_value(num1, num2, num3)


if num1 > num2 and num1 > num3:
    highest_number = num1

elif num2 > num1 and num2 > num3:
    highest_number = num2

else:
    highest_number = num3

print("The highest number inputted is", highest_number)
