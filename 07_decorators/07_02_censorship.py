# Create a decorator that censors potentially offensive words from a text.
# For example, assuming that "shoot" was considered an offensive word:
# A function that would normall return this text:
#    "I bumped my toe! Shoot!"
# Would, after decorating it with `@censor()`, return:
#    "I bumped my toe! S****!"

def censor(text):
    def wrapper():

        bad_words = ("shoot", "crap", "dang")

        lower_text = text.lower()
        for bad_word in bad_words:
            index = lower_text.find(bad_word)
            if index != -1:
                censored_word = lower_text[index] + "*" * (len(bad_word) - 1)
                lower_text = lower_text.replace(bad_word, censored_word)
        
        return lower_text
    
    return wrapper

print(censor("Oh dang, my foot hurts like crap!")())