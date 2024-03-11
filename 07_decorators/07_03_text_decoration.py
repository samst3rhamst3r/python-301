# Write a decorator that literally decorates text output.
# Make it so the symbol it uses can be an argument to the decorator
#
# The output of a function that returns `"Hello"` that has been
# decorated like with `@decorate("*")` should look like this:
#
# ******************************
# Hello
# ******************************

def decorate(char):
    def decorator_func(func):
        def wrapper(*args, **kwargs):
            s = char * 20 + "\n"
            s += func(*args, **kwargs) + "\n"
            s += char * 20
            return s
        return wrapper
    return decorator_func

@decorate("*")
def say_hello():
    return "Hello!"

print(say_hello())