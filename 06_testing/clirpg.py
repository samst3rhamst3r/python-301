
import textwrap, random, sys

class Creature:

    def __init__(self, name: str, max_hp: int, attack: int, defense: int, curr_hp=None) -> None:
        self.name = name
        self.max_hp = max_hp
        self.attack_lv = attack
        self.defense_lv = defense
        if curr_hp is None:
            self.curr_hp = max_hp
    
    def __str__(self):
        return textwrap.dedent(f"""
        {self.__class__.__name__}
            Name: {self.name}
            Max HP: {self.max_hp}
            Curr HP: {self.curr_hp}
            Attack: {self.attack_lv}
            Defense: {self.defense_lv}
        """)

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name}, max_hp={self.max_hp}, attack={self.attack_lv}, defense={self.defense_lv}, curr_hp={self.curr_hp}"

    def get_name(self):
        return self.name
    
    def get_curr_hp(self):
        return self.curr_hp

    def get_max_hp(self):
        return self.max_hp
    
    def take_dmg(self, amt: int):
        self.curr_hp = max(0, self.curr_hp - amt)
        return self.curr_hp
        
    def attack(self):
        return random.randint(0, self.attack_lv)
    
    def defend(self):
        return random.randint(0, self.defense_lv)
    
    def is_dead(self):
        return self.curr_hp <= 0

class Hero(Creature):
    
    def __init__(self, name: str, max_hp: int, attack: int, defense: int, pack=None, equipped_items=None) -> None:
        super().__init__(name, max_hp, attack, defense)
        self.pack = pack
        self.equipped_items = equipped_items

        if pack is None:
            self.pack = {}
        if equipped_items is None:
            self.equipped_items = {}
    
    def __str__(self):
        return super().__str__() + \
            f"    Pack: {self.pack}\n" + \
            f"    Equipped: {self.equipped_items}\n"
    
    def __repr__(self):
        return super().__repr__() + f", pack={self.pack.__repr__()}, equipped_items={self.equipped_items.__repr__()})"

    def get_equipped_items(self):
        return self.equipped_items

    def heal(self, amt: int):
        self.curr_hp = min(self.max_hp, self.curr_hp + amt)
        
    def attack(self):
        att_lv = super().attack()
        for item in self.equipped_items.values():
            att_lv = item.att_func(att_lv)
        return att_lv

    def defend(self):
        def_lv = super().defend()
        for item in self.equipped_items.values():
            def_lv = item.def_func(def_lv)
        return def_lv

    def add_to_pack(self, item):
        
        item_name = item.get_name()
        if item_name in self.pack.keys():
            self.pack[item_name]["quantity"] += 1
        else:
            self.pack[item_name] = {"item": item, "quantity": 1}

        print(f"{item.name.capitalize()} added to pack.")

    def rem_from_pack(self, item_name: str):

        if item_name in self.pack.keys():
            
            self.pack[item_name]["quantity"] -= 1
            print(f"{item_name.capitalize()} removed from pack.")  
        
            if self.pack[item_name]["quantity"] == 0:
                return self.pack.pop(item_name)["item"]
            else:
                return self.pack[item_name]["item"]

        else:
            print(f"You do not have a(n) {item_name.capitalize()}.")

    def equip_items(self):
        
        for item_name in self.pack.keys():
            item = self.pack[item_name]["item"]
            if item is not None:
                self.equipped_items[item_name] = item
                print(f"{item.get_name().capitalize()} equipped.")
        
        for item_name in self.equipped_items.keys():
            self.rem_from_pack(item_name)
    
    def unequip_items(self):
        
        for item_name in self.equipped_items.keys():
            item = self.equipped_items[item_name]
            self.add_to_pack(item)
            print(f"{item_name.capitalize()} unequipped and added to pack.")
        
        self.equipped_items.clear()

class Opponent(Creature):
    
    def __repr__(self):
        return super().__repr__() + ")"

class Item:
    
    def __init__(self, name: str, consumable=False, att_effect=None, def_effect=None, rest_effect=None) -> None:
        self.name = name
        self.consumable = consumable
        self.att_effect = att_effect
        self.def_effect = def_effect
        self.rest_effect = rest_effect
    
        default_func = lambda x: x
        if att_effect is None:
            self.att_effect = default_func
        if def_effect is None:
            self.def_effect = default_func
        if rest_effect is None:
            self.rest_effect = default_func

    def get_name(self):
        return self.name
    
    def is_consumable(self):
        return self.consumable

    def att_func(self, *args, **kwargs):
        return self.att_effect(*args, **kwargs)

    def def_func(self, *args, **kwargs):
        return self.def_effect(*args, **kwargs)
    
    def rest_func(self, *args, **kwargs):
        return self.rest_effect(*args, **kwargs)
    
class Room:
    
    def __init__(self, room_no: int, item: Item = None, enemy: Opponent = None) -> None:
        self.room_no = room_no
        self.item = item
        self.enemy = enemy
        self.joined_rms = None

    def set_joined_rms(self, joined_rms: dict) -> None:
        self.joined_rms = joined_rms

    def get_joined_rms(self) -> tuple:
        return tuple(rm.room_no for rm in self.joined_rms)

    def get_rm(self, room_no: int):
        return self.joined_rms[room_no]

    def get_room_no(self):
        return self.room_no
    
    def get_item(self):
        return self.item
    
    def get_enemy(self):
        return self.enemy

    def rmv_enemy(self):
        self.enemy = None

    def acquire_item(self):
        item = self.item
        self.item = None
        return item

    def __repr__(self):
        return f"{self.__class__.__name__}(room_no={self.room_no}, item={self.item.name}, enemy={self.enemy}, joined_rms={self.get_joined_rms()})"

class Map:

    def __init__(self, rooms: dict, hero: Hero) -> None:
        self.rooms = rooms
        self.hero = hero
        self.hero_loc = self.rooms[1]
    
    def get_curr_rm_no(self) -> int:
        return self.hero_loc.get_room_no()
    
    def get_curr_rm_enemy(self) -> Opponent | None:
        return self.hero_loc.get_enemy()
    
    def get_curr_rm_item(self) -> Item | None:
        return self.hero_loc.get_item()
    
    def get_joined_rms(self) -> tuple:
        return self.hero_loc.get_joined_rms()

    def get_hero(self) -> Hero:
        return self.hero

    def get_hero_loc(self) -> Room:
        return self.hero_loc
    
    def is_hero_dead(self) -> int:
        return self.hero.is_dead()
    
    def move_hero_to(self, room_no: int) -> None:
        self.hero_loc = self.rooms[room_no]
    
    def acquire_rm_item(self):
        self.hero.add_to_pack(self.hero_loc.acquire_item())

    def rmv_curr_enemy(self):
        self.hero_loc.rmv_enemy()

def battle(hero, enemy):
    
    print(f"You are battling the {enemy.get_name()}!")
    
    user_input = get_user_input("Do you wish to equip your items? (y/n)")
    if user_input == "y":
        hero.equip_items()
    
    enemy_name = enemy.get_name()
    while True:
        
        print(f"You have {hero.get_curr_hp()} of {hero.get_max_hp()} left.")
        if "potion" in hero.get_equipped_items().keys():
            user_input = get_user_input("Would you like to use a potion?")
            if user_input == 'y':
                hero.heal(hero.get_equipped_items()["potion"].rest_effect(hero.get_curr_hp()))

        hero_attack = hero.attack()
        hero_defense = hero.defend()
        
        enemy_attack = enemy.attack()
        enemy_defense = enemy.defend()

        hero_dmg = max(0, enemy_attack - hero_defense)
        enemy_dmg = max(0, hero_attack - enemy_defense)

        hero.take_dmg(hero_dmg)
        enemy.take_dmg(enemy_dmg)

        print(f"You attack for {hero_attack} damage! The {enemy_name} defends against {enemy_defense}!")
        print(f"The {enemy_name} attacks for {enemy_attack} damage! You defend against {hero_defense}!")
        print(f"You take {hero_dmg} damage! The {enemy_name} takes {enemy_dmg} damage!")
        
        if enemy.is_dead():
            print(f"The {enemy_name} is dead!")
        
        if hero.is_dead():
            print("You are dead!")
            return False
        elif enemy.is_dead():
            print("You won the battle!")
            return True
        else:
            print(f"You have {hero.get_curr_hp()} HP left.")
            print(f"The {enemy_name} has {enemy.get_curr_hp()} HP left.")
            user_input = get_user_input("Would you like to (c)ontinue the battle or (r)etreat?", valid_resps=('c', 'r'))   
            if user_input == 'r':
                print("You hastily retreat!")
                return False     

def get_map(name):
    
    ghoul = Opponent("ghoul", 5, 2, 1)
    skeleton = Opponent("skeleton", 3, 1, 1)
    dragon = Opponent("dragon", 6, 3, 2)
    
    sword = Item("sword", att_effect=lambda attack: attack + 2)
    shield = Item("shield", def_effect=lambda defense: defense + 2)
    potion = Item("potion", consumable=True, rest_effect=lambda hp: hp + 2)
    
    room1 = Room(1, item=potion)
    room2 = Room(2, item=sword, enemy=ghoul)
    room3 = Room(3, enemy=dragon)
    room4 = Room(4, item=shield)
    room5 = Room(5, enemy=skeleton)
    
    room1.set_joined_rms((room2, room3))
    room2.set_joined_rms((room1, room3, room4))
    room3.set_joined_rms((room1, room2, room5))
    room4.set_joined_rms((room2, room5))
    room5.set_joined_rms((room3, room4))

    room_dict = {rm.room_no: rm for rm in (room1, room2, room3, room4, room5)}

    return Map(room_dict, Hero(name, max_hp=5, attack=3, defense=2))

def get_user_input(input_str: str, *, valid_resps: tuple = ('y', 'n'), cast_type: type = str):

    while True:
        
        print(input_str)
        user_input = input().lower()
        
        try:
            user_input = cast_type(user_input)
        except ValueError:
            print(f"Invalid input. Input must be of type {cast_type}.")
        else:
            if user_input not in valid_resps:
                print(f"Invalid response. Valid responses include: {valid_resps}. Try again.", file=sys.stderr)
            else:
                return user_input

def move_to_new_room(map):
    
    rm_select = get_user_input(f"Where would you like to go? Room options: {map.get_joined_rms()}", valid_resps=map.get_joined_rms(), cast_type=int)
    map.move_hero_to(rm_select)
    print(f"You have moved to room number {rm_select}.")

def explore(map):
    
    print("What would you like to do? Please choose from the following options:")
    print("1. Look around")
    print("2. Move to a new room")
    
    user_input = get_user_input("", valid_resps=tuple(range(1, 3)), cast_type=int)

    match user_input:
        case 1:
            item = map.get_curr_rm_item()
            if item is not None:
                print(f"You found a(n) {item.get_name()}. You put it in your pack.")
                map.acquire_rm_item()
            else:
                print("There are no items in this room. Please move to another room.")
        case 2:
            move_to_new_room(map)

def encounter_rm(map):
    
    rm = map.get_hero_loc()

    print(f"You are in room {rm.get_room_no()}.")
    
    hero = map.get_hero()
    enemy = rm.get_enemy()

    if enemy is not None:
            
        resp = get_user_input(f"There is a(n) {enemy.get_name()}! Do you wish to fight it? (y/n)")
        
        if resp == "y":
            
            won = battle(hero, enemy)
            
            if won:
                map.rmv_curr_enemy()
                explore(map)
            elif not hero.is_dead():
                    print(f"Better get outta there before the {enemy.get_name()} kills you!")
                    move_to_new_room(map)

        else:
            print("Well then, you best run away, y'all!")
            move_to_new_room(map)
    
    else:
        explore(map)
        
def init_game():

    print()
    print("Welcome to the D&D CLI game! Please input a name for your character:")
    name = input()
    print(f"Hello, {name}! You're about to start an adventure!")
    print()

    map = get_map(name)

    while True:

        encounter_rm(map)

        if map.get_hero().is_dead():
            print("Game over! You are dead.")
            break

        resp = get_user_input("Would you like to quit? (y/n)")
        if resp == "y":
            break

    print(f"Thanks for playing, {name}! Goodbye.")

if __name__ == "__main__":

    init_game()
