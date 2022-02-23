valid = False

while not valid:
    try:
        times_tables = int(input("What number would you like to times table? "))
        valid = True

    except ValueError:
        print("Please input int")


valid = False
while not valid:
    try:
        max_value = int(input("what is the max value of your times table"))
        valid = True
    except ValueError:
        print("Please input int")


max_value = max_value + 1
answer = 0

print("Here is the {} times tables".format(times_tables))

for x in range(1, max_value):
    answer = x * times_tables
    print("{} X {} is {}".format(x, times_tables, answer))
