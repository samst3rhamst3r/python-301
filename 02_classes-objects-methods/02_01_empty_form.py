# A good way to think about how classes are blueprints of objects is to think of
# an empty form, for example one that you would get at a doctor's office.
# The empty form contains all the placeholders that define what information
# you need to fill to complete the form. If you fill it correctly, then you've
# successfully instantiated a form object, and your completed form now holds
# information that is specific to just you.
# Another patient's form will follow the same blueprint, but hold different info.
# You could say that every patient's filled form instance is part of the same
# empty form blueprint class that the doctor's office provided.
#
# Model such an application form as a Python class below, and instantiate
# a few objects from it.

class Form:

    def __init__(self, name: str, age: int, gender: str) -> None:
        
        self.name = name
        self.age = age
        self.gender = gender
    
me = Form("Sam", 34, "m")
someone_else = Form("Barbara", 57, "f")

print(me)
print(someone_else)