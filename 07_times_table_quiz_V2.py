def correct_input(question):
    valid = False
    while not valid:
        try:
            response = int(input(question))
            return response
            
        except ValueError:
            print("Error please enter a whole number\n")
            
practice = correct_input("What number would you like to test? \n")

max_value = correct_input("What times table would you like to go up to? \n")

print("Here are the {} times tables up to {} \n".format(practice, max_value))

for x in range(1, max_value + 1):
    answer = x * practice
    user_answer = correct_input("What is {} x {}\n".format(x, practice))
    
    if user_answer == answer:
        print("Correct\n")
    else:
        print("Incorrect the answer was {}\n".format(answer))
