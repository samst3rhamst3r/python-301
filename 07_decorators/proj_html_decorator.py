
def tagify(tag):
    def decorator(func):
        def wrapper(*args, **kwargs):
            return f"<{tag}>{func(*args, **kwargs)}</{tag}>"
        return wrapper
    return decorator

@tagify("p")
def greet(name):
    return f"Hello, {name}"

print(greet("Bessy"))  # OUTPUT: <p>Hello, Bessy</p>