# Write a script that takes in two numbers from the user and calculates the quotient.
# Use a try/except statement so that your script can handle:
#
# - if the user enters a string instead of a number
# - if the user enters a zero as the divisor
#
# Test it and make sure it does not crash when you enter incorrect values.

while True:
    try:
        dividend = int(input("Dividend: "))
        divisor = int(input("Divisor: "))
        print(dividend / divisor)
    except ValueError:
        print("Input must be numbers")
    except ZeroDivisionError:
        print("Divisor cannot be 0")