# Write a script with three classes that model everyday objects.
# - Each class should have an `__init__()` method that sets at least 3 attributes
# - Include a `__str__()` method in each class that prints out the attributes
#     in a nicely formatted string.
# - Overload the `__add__()` method in one of the classes so that it's possible
#     to add attributes of two instances of that class using the `+` operator.
# - Create at least two instances of each class.
# - Once the objects are created, change some of their attribute values.
#
# Be creative. Have some fun. :)
# Using objects you can model anything you want:
# Animals, paintings, card games, sports teams, trees, people etc...

import random

class Family:

    def __init__(self, surname, parents: list, children: list = []) -> None:
        self.surname = surname
        self.parents = parents
        self.children = children
    
    def separate(self):
        if len(self.parents) > 1:
            self.parents.pop()
            self.surname = self.parents[0].last_name

    def have_child(self, gender):
        self.children.append(Person("[Unknown]", self.surname, 0, gender))

    def __str__(self):
        s = [f"The {self.surname} family is composed of:"]
        for parent in self.parents:
            s.append("\t" + str(parent))
        for child in self.children:
            s.append("\t" + str(child))
        return "\n".join(s)

class Person:

    def __init__(self, first_name, last_name, age, gender) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender

    def __add__(self, other):

        new_surname = f"{self.last_name}-{other.last_name}"

        if self.gender != other.gender:
            rand_int = random.randint(0, 1)
            if rand_int == 0:
                baby_gender = "m"
            else:
                baby_gender = "f"
            return Family(new_surname, [self, other], [Person("new kid", new_surname, 0, baby_gender)])
        else:
            return Family(new_surname, [self, other])
    
    def __str__(self) -> str:
        return f"Name: {self.first_name} {self.last_name}; Age: {self.age}; Gender: {self.gender}"

    def legally_change_name(self, first_name = None, last_name = None):
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
    
    def celebrate_birthday(self):
        self.age += 1

class CardGame:

    def __init__(self, game_name, family) -> None:
        self.game_name = game_name
        self.family = family
    
    def __str__(self) -> str:
        return f"The {self.family.surname} family is playing {self.game_name}."

    def play_game(self):
        print("Everyone hates each other now! The family is separating!")
        self.family.separate()

sam = Person("Sam", "Turner", 34, "m")
bf = Person("Shawn", "White", 35, "m")

print(sam)
print(bf)

f = sam + bf
print(f)
print("You're having a child!")
f.have_child("m")
print(f)

sam.celebrate_birthday()
print("Happy birthday Sam!")
print(f)

card_game = CardGame("Monopoly", f)
print(card_game)
card_game.play_game()

print(f)