word = "sandwich"
count_e = 0

user_letter = input("What letter would you like to test for? ")

for letter in word:
    if letter == user_letter:
        count_e = count_e + 1

print("{} appears {} in the word".format(user_letter, count_e))
