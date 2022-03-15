def value_checker(question):
    valid = False
    while not valid:
        try:
            response = int(input(question))
            return response

        except ValueError:
            print("Please input whole number \n")


times_tables = value_checker("What number would you like to times table? ")

max_value = value_checker("what is the max value of your times table? ")

max_value = max_value + 1
answer = 0

print("Here is the {} times tables".format(times_tables))

for x in range(1, max_value):
    answer = x * times_tables
    print("{} X {} is {}".format(x, times_tables, answer))
