# Read in the first number from `integers.txt`
# and perform a calculation with it.
# Make sure to catch at least two possible Exceptions (`IOError` and `ValueError`)
# with specific `except` statements, and continue to do the calculation
# only if neither of them applies.

import pathlib

file_name = 'integers.txt'

file_path = pathlib.Path(__file__).parent / file_name

try:
    f = open(file_path, 'r')
    line = int(f.readline())
except IOError:
    print("Could not open the file")
except ValueError:
    print("Value is not readable. Is probably not an integer")
finally:
    print(line + 5)