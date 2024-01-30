# Build a very basic Pokémon class that allows you to simulate battles
# in a Rock-Paper-Scissors game mechanic, as well as feed your Pokémon.
#
# The class should follow these specifications:
#
# - Each Pokemon should have a `name`, `primary_type`, `max_hp` and `hp`
# - Primary types should be limited to `water`, `fire` and `grass`
# - Implement a `battle()` method based on rock-paper-scissors that
#   decides who wins based only on the `primary_type`:
#       water > fire > grass > water
# - Display messages that explain who won or lost a battle
# - If a Pokemon loses a battle, they lose some of their `hp`
# - If you call the `feed()` method on a Pokemon, they regain some `hp`

import enum

class PokemonType(enum.Enum):
    WATER = enum.auto()
    FIRE = enum.auto()
    GRASS = enum.auto()

class Pokemon:

    def __init__(self, name: str, primary_type: PokemonType, max_hp: int) -> None:
        self.name = " ".join(name.strip().lower().capitalize().split())
        self.primary_type = primary_type
        self.max_hp = max_hp
        self.hp = self.max_hp

    def battle(self, other):
        
        print(f"{self.name} battles {other.name}!")

        if self.primary_type == other.primary_type:
            print("Tie! No damage is done.")
        else:
            win = None
            if self.primary_type is PokemonType.WATER:
                win = other.primary_type is PokemonType.FIRE
            elif self.primary_type is PokemonType.FIRE:
                win = other.primary_type is PokemonType.GRASS
            else:
                win = other.primary_type is PokemonType.WATER
            
            if win:
                Pokemon._determine_winner(self, other)
            else:
                Pokemon._determine_winner(other, self)

    def feed(self):
        print(f"You feed the {self.name}!")
        self.hp += 2
        if self.hp > self.max_hp:
            self.hp = self.max_hp
        print(f"{self.name}'s HP is now {self.hp}")

    def __str__(self):
        return f"{self.name}: Max HP ({self.max_hp}); Current HP: ({self.hp})"

    @staticmethod
    def _determine_winner(winner, loser):
        print(f"{winner.name}'s attack is super effective!'")
        loser.hp -= 2
        if loser.hp <= 0:
            print(f"{winner.name} has killed the {loser.name}")
        else:
            print(f"{loser.name}'s HP is now {loser.hp}")

if __name__ == "__main__":
    
    bulbasaur = Pokemon("Bulbasaur", PokemonType.GRASS, 6)
    charmander = Pokemon("Charmander", PokemonType.FIRE, 5)
    squirtle = Pokemon("Squirtle", PokemonType.WATER, 6)

    bulbasaur.battle(charmander)
    bulbasaur.battle(squirtle)
    charmander.battle(squirtle)
    charmander.battle(charmander)

    charmander.feed()
    charmander.feed()

    print(bulbasaur)
    print(squirtle)
    print(charmander)