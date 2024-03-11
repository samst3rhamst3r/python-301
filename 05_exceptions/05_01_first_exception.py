# Write a script that generates an exception.
# Handle this exception with a try/except block.
# For example:
#
# list_ = ["hello world!"]
# print(list_[1])
#
# This raises and exception that needs to be handled.

x = 10
y = 0

try:
    result = x / y
except ZeroDivisionError:
    print("Nooooo you divided by 0")