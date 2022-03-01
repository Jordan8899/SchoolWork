def value_checker(value):
    valid = False
    while not valid:
        try:
            response = int(input(value))
            return response

        except ValueError:
            print("Error please enter a whole number\n")

def marker(a, b, c):
    if c == "*":
        answer = a * b
        print("The answer is:", answer)
        return answer

    elif c == "-":
        answer = a - b
        print("The answer is:", answer)
        return answer

    elif c == "/":
        answer = a / b
        print("The answer is:", answer)
        return answer

    elif c == "+":
        answer = a + b
        print("The answer is:", answer)
        return answer

    else:
        print("Sorry there was an error\n")

marking = False
while not marking:
    num1 = value_checker("What's the 1st number? ")
    num2 = value_checker("What's the 2nd number? ")
    operator = input("Please input one of the following '+' '*' '/' '-' ")
    marker(num1, num2, operator)
    true_false = input("Would you like to stop marking if so type 'Y' if not input anything: ").strip().lower()
    if true_false == "y":
        marking = True
