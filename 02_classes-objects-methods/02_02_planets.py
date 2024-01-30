# Create a `Planet()` class that models attributes and methods of
# a planet object.
# Use the appropriate dunder method to get informative output with `print()`

class Planet():
    
    def __init__(self, name, yr_len_earth_days) -> None:
        self.name = name
        self.yr_len_earth_days = yr_len_earth_days
    
    def __str__(self):
        return f"{self.name} has a year length of {self.yr_len_earth_days} earth days."
    
    def __repr__(self):
        return f"Planet(name={self.name}, yr_length_earth_days={self.yr_len_earth_days})"

earth = Planet("Earth", 365)
saturn = Planet("Saturn", 744) # Actually I don't know how many earth days are in Saturn's year

print(earth)
print(repr(saturn))