# Write a decorator function that wraps text output into quotes, e.g.:
# Hello world! ----> "Hello World!"
# You can use it to create quotes from text output.

def wrap_in_quotes(msg):
    def wrapper_func():
        return f"\"{msg}\""
    return wrapper_func

print(wrap_in_quotes("Hello world!")())
