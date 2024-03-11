# Create a script that asks a user to input an integer, checks for the
# validity of the input type, and displays a message depending on whether
# the input was an integer or not.
# The script should keep prompting the user until they enter an integer.

while True:

    value = input("Please input an integer: ")
    if not value.isdigit():
        print("Sorry. Input must be an integer")
    else:
        print("Yay you input an integer")
        break