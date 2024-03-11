# In this exercise, you will practice both File I/O as well as using Exceptions
# in a real-world scenario.
#
# This folder contains another folder called `books/` that contains three text files
# of books from Project Gutenberg:
# 1. war_and_peace.txt
# 2. pride_and_prejudice.txt
# 3. crime_and_punishment.txt
#
# 1) Open `war_and_peace.txt`, read the whole file content and store it in a variable
# 2) Open `crime_and_punishment.txt` and overwrite the whole content with an empty string
# 3) Loop over all three files and print out only the first character each. Your program
#    should NEVER terminate with a Traceback.
#     a) Which exception can you expect to encounter? Why?
#     b) How do you catch it to avoid the program from terminating with a traceback?

import pathlib

base_path = pathlib.Path(__file__).parent / "books"

with open(base_path / "war_and_peace.txt", 'r') as war:
    war_txt = war.read()

with open(base_path / "crime_and_punishment.txt", 'w') as pride:
    pride.write("")

try:
    pride = open(base_path / "pride_and_prejudice.txt", 'r')
    crime = open(base_path / "crime_and_punishment.txt", 'r')

    print(war_txt[0])
    print(pride.read()[0])
    print(crime.read()[0])
except IndexError as e:
    print(e)
finally:
    pride.close()
    crime.close()