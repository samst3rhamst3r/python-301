# Build on top of the censorship exercise and change your decorator function
# so that you can pass the words it should censor when decorating a function, e.g.:
# `@censor("shoot", "crab")` would censor the words "shoot" and "crab".

def censor(*bad_words):
    def decorator(func):
        def wrapper(*args, **kwargs):
            
            lower_text = func(*args, **kwargs).lower()
            
            for bad_word in bad_words:
                index = lower_text.find(bad_word)
                if index != -1:
                    censored_word = lower_text[index] + "*" * (len(bad_word) - 1)
                    lower_text = lower_text.replace(bad_word, censored_word)
            
            return lower_text
        
        return wrapper
    return decorator

@censor("shoot", "crap")
def stub_my_toe():
    return "Oh shoot, my foot hurts like crap!"

print(stub_my_toe())