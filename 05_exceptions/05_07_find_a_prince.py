# Write a custom exception  that inherits from `Exception()`
# Open and read in the content of the book `.txt` files in the `books/` folder
# like you did in the previous exercise.
# Raise your `PrinceException()` if the first 100 characters of a book
# contain the string "Prince".

import pathlib

class PrinceException(Exception):
    pass

base_path = pathlib.Path(__file__).parent / "books"

READ_SIZE = 100

try:
    war = open(base_path / "war_and_peace.txt")
    pride = open(base_path / "pride_and_prejudice.txt")
    crime = open(base_path / "crime_and_punishment.txt")

    war_txt = war.read(READ_SIZE)
    pride_txt = pride.read(READ_SIZE)
    crime_txt = crime.read(READ_SIZE)

    if "Prince" in war_txt:
        raise PrinceException("War and peace contains a prince")
    elif "Prince" in pride_txt:
        raise PrinceException("Pride and prejudice contains a pricne")
    elif "Prince" in crime_txt:
        raise PrinceException("Crime and punishment contains a prince")
except Exception as e:
    print(e)
finally:
    war.close()
    pride.close()
    crime.close()