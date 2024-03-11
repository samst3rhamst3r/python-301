# Create a custom decorator function that records the execution time of
# the decorated function and prints the time to your console when the function
# has finished execution.

import timeit

def time_it(func):
    def wrapper(*args, **kwargs):
        start = timeit.default_timer()
        result = func(*args, **kwargs)
        end = timeit.default_timer()
        print(f"Time to execute: {end - start} seconds")
        return result
    return wrapper

@time_it
def f():
    print("Happy execution")

f()