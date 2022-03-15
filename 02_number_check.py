def int_check(age):
    while True:
        try:
            response = int(input(age))

            if response > 0:
                return response
            else:
                print("Please input your actual age\n")

        except ValueError:
            print("Error\n")


user_age = int_check("How old are you? ")

if user_age in range(1, 6):
    print("You are too young to be doing this by yourself")
