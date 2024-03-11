# Write a script that demonstrates a try/except/else statement.
# For example, you can revisit the course module about database interactions
# and include a try/except/else statement based on what to do whether or not
# the database connection can be established.

import sqlalchemy
from pprint import pprint

engine = sqlalchemy.create_engine(f"mysql+pymysql://python:@localhost/sakila")

try:
    connection = engine.connect()
except Exception:
    print("Could not connect")
finally:
    connection.close()
    print("Yay, you did stuff")

    