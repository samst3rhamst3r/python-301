
import enum, random

def check_user_input(input_str, *, valid_resps: tuple = ('y', 'n'), cast_type: type = str):
    while True:
        print(input_str)
        user_input = input().lower()
        try:
            cast_input = cast_type(user_input)
        except ValueError:
            print(f"Error. Value must be of type {cast_type.__name__}. Try again.")
        else:
            if (cast_input is str and cast_input in tuple(c.lower() for c in valid_resps)) or \
                cast_input in valid_resps:
                return cast_input
            else:
                print(f"Valid responses include: {valid_resps}. Try again")

class CardSuit(enum.Enum):
    """An Enum class to identify the valid types of Card Suits, including Jokers
    """
    SPADES = enum.auto()
    CLUBS = enum.auto()
    DIAMONDS = enum.auto()
    HEARTS = enum.auto()
    JOKER = enum.auto()

    def is_black(self):
        """Returns whether the current suit is black"""
        return self in (self.__class__.SPADES, self.__class__.CLUBS)
    
    def is_red(self):
        """Returns whether the current suit is red"""
        return self in (self.__class__.DIAMONDS, self.__class__.HEARTS)
    
    def is_joker(self):
        """Returns whether the current 'suit' is Joker"""
        return self is self.__class__.JOKER

    def __str__(self):
        """Default string representations only include first 3 characters of the suit name,
        in order to keep string widths consistent
        """
        return self.name[:3]
    
    def __repr__(self):
        return f"{self.__class__.__name__}.{self.name}"

class CardValue(enum.Enum):
    """An Enum class to classify the face value of a card, including Jokers"""
    ACE = enum.auto()
    TWO = enum.auto()
    THREE = enum.auto()
    FOUR = enum.auto()
    FIVE = enum.auto()
    SIX = enum.auto()
    SEVEN = enum.auto()
    EIGHT = enum.auto()
    NINE = enum.auto()
    TEN = enum.auto()
    JACK = enum.auto()
    QUEEN = enum.auto()
    KING = enum.auto()
    JOKER = enum.auto()

    def is_joker(self):
        """Returns if the 'value' is Joker"""
        return self is self.__class__.JOKER
    
    def is_face(self):
        """Returns if the value is A, J, Q, K"""
        return self in (self.__class__.ACE, self.__class__.JACK, self.__class__.QUEEN, self.__class__.KING)

    def is_num(self):
        """Returns is the value is numeric"""
        return not self.is_face() and not self.is_joker()
    
    def __gt__(self, other):
        return self.value > other.value
    
    def __ge__(self, other):
        return self.value >= other.value

    def __lt__(self, other):
        return self.value < other.value
    
    def __le__(self, other):
        return self.value <= other.value
    
    def __eq__(self, other):
        return self.value == other.value

    def __ne__(self, other):
        return self.value != other.value
    
    def __str__(self):
        """Returns a string representation of the value"""
        match self:
            case CardValue.ACE: return "A"
            case CardValue.TWO: return "2"
            case CardValue.THREE: return "3"
            case CardValue.FOUR: return "4"
            case CardValue.FIVE: return "5"
            case CardValue.SIX: return "6"
            case CardValue.SEVEN: return "7"
            case CardValue.EIGHT: return "8"
            case CardValue.NINE: return "9"
            case CardValue.TEN: return "10"
            case CardValue.JACK: return "J"
            case CardValue.QUEEN: return "Q"
            case CardValue.KING: return "K"
            case _: return ""

    def __repr__(self):
        return f"{self.__class__.__name__}.{self.name}"
    
class Card:
    """A class that describes a single playing card with a suit and value"""

    # Color and string formatting for when printing card information
    _black = u"\u001b[47m\u001b[30m"
    _red = u"\u001b[41m\u001b[37m"
    _clear = u"\u001b[0m"
    _color_char_len = len(_black + _clear)
    _pad_len = len(str(CardValue.TEN) + " of " + str(CardSuit.CLUBS))

    @classmethod
    def get_empty_str(cls):
        """Class method to return an empty string the size of the pad length 
        of the longest string representation of a card.
        """
        return "".ljust(cls._pad_len)

    @classmethod
    def get_pad_len(cls):
        """Class method to return the pad length 
        of the longest string representation of a card.
        """
        return cls._pad_len
    
    def __init__(self, value: CardValue, suit: CardSuit) -> None:
        """
        Required params:
            value: Enum type CardValue
            suit: Enum type CardSuit
        """
        self.value = value
        self.suit = suit

        self._formatted_color = None
        if self.is_black():
            self._formatted_color = self._black
        elif self.is_red():
            self._formatted_color = self._red
    
    def get_value(self):
        """Returns the CardValue Enum type of this card"""
        return self.value
    
    def get_suit(self):
        """Returns the CardSuit Enum type of this card"""
        return self.suit

    def is_face(self):
        """Returns bool of whether this card is in values A, J, Q, K"""
        return self.value.is_face()

    def is_num(self):
        """Returns bool of whether this card is in values 2-10"""
        return self.value.is_num()
    
    def is_black(self):
        """Returns bool of whether this card is Spades or Clubs"""
        return self.suit.is_black()
    
    def is_red(self):
        """Returns bool of whether this card is Hearts or Diamonds"""
        return self.suit.is_red()
    
    def is_joker(self):
        """Returns bool of whether this card is a Joker"""
        return self.suit.is_joker()

    def is_same_suit(self, other):
        """Returns bool to determine if both cards have the same suit"""
        return self.suit is other.suit
    
    def is_same_color(self, other):
        """Returns bool to determine if both cards are the same color"""
        return (self.is_black() and other.is_black()) or (self.is_red() and other.is_red())

    def is_dif_color(self, other):
        """Returns bool to determine if both cards are different colors"""
        return not self.is_same_color(other)
    
    def __str__(self):
        """Format of the string is '[value] of '[suit]'
        If the card is a joker, will simply return 'JOK'
        """
        if self.is_joker():
            return str(self.suit).ljust(self._pad_len)
        else:
            return f"{self._formatted_color}{self.value} of {self.suit}{self._clear}".ljust(self._pad_len + self._color_char_len)
        
    def __repr__(self):
        return f"{self.__class__.__name__}(value={repr(self.value)}, suit={repr(self.suit)})"

    def __eq__(self, other):
        return self.value == other.value
    
    def __ne__(self, other):
        return self.value != other.value
    
    def __gt__(self, other):
        return self.value > other.value
    
    def __ge__(self, other):
        return self.value >= other.value
    
    def __lt__(self, other):
        return self.value < other.value
    
    def __le__(self, other):
        return self.value <= other.value

class Deck(list):
    """A subclass of list that includes various deck-type methods,
    such as 'shuffle' and 'draw'
    """

    def __init__(self, deck: list = None, *, include_jokers=False) -> None:
        
        if deck is None:
            
            super().__init__([])
            
            for suit in CardSuit:
                if suit is not CardSuit.JOKER:
                    for value in CardValue:
                        if value is not CardValue.JOKER:
                            self.append(Card(value, suit))
            if include_jokers:
                for _ in range(2):
                    self.append(Card(CardValue.JOKER, CardSuit.JOKER))
        
        else:
            super().__init__(deck)
            
    def shuffle(self):
        random.shuffle(self)
    
    def draw(self):
        return self.pop()
    
    def is_empty(self):
        return len(self) == 0

    def index(self, value: str, suit=None):
        value = value.upper()
        for i, c in enumerate(self):
            if str(c.get_value()) == value and (suit is None or c.suit is suit):
                return i
            
    def __str__(self):
        return ", ".join(self)
    
    def __repr__(self):
        return f"{self.__class__.__name__}(deck={repr(self)})"
    
    def __getitem__(self, key):
        return super().__getitem__(key)
        
class Player:
    """A class for a single player of a card game
    
    Attributes:
        name: string name of the player
        hand: the list() of Cards in the player's hand
    """
    
    def __init__(self, name: str, hand=[]) -> None:
        self.name = name 
        self.hand = hand
       
    def add_to_hand(self, card):
        self.hand.append(card)

    def print_hand(self):
        print(f"***************  PLAYER HAND   ***************")
        for i, card in enumerate(self.hand):
            print(f"{i + 1}. {card}")
        print(f"***************  PLAYER HAND   ***************")

    def get_hand_len(self):
        return len(self.hand)

    def get_card(self, index):
        return self.hand[index]
    
    def remove_card(self, index):
        return self.hand.pop(index)

    def __str__(self):
        return f"Player: {self.name}; Hand: {self.hand}"
    
    def __repr__(self):
        return f"{self.__class__.__name__}(name='{self.name}', hand={self.hand})"

class CardGame:

    def __init__(self, players: tuple) -> None:
        self.players = players
        
class Solitaire(CardGame):
    """A subclass of CardGame that plays a CLI version of Solitaire
    
    Attributes:
        discard_pile: an initially empty Deck() of cards
        suit_piles: a dictionary for each suit pile to be filled throughout the game, 
            where each entry is of the format - key=CardSuit, value=Deck()
        draw_pile: a full Deck() that is initially shuffled, then delt according to 
            game rules
        game_piles: a tuple() 7 piles of playable piles, where each pile is formatted 
            as a dictionary with each entry containing an 'up' and 'down' Deck() that
            defines the faceup and facedown card stacks throughout the game
    """
    _separator_str = " | "

    def __init__(self, player) -> None:
        super().__init__((player,))
        
        self.discard_pile = Deck([])
        self.suit_piles = { CardSuit.CLUBS.name: Deck([]), \
                            CardSuit.SPADES.name: Deck([]), \
                            CardSuit.HEARTS.name: Deck([]), \
                            CardSuit.DIAMONDS.name: Deck([])}

        self.draw_pile = Deck()
        self.draw_pile.shuffle()

        self.game_piles = tuple({"up": Deck([]), "down": Deck([])} for _ in range(7))
        for i in range(len(self.game_piles)):
            
            self.game_piles[i]["up"].append(self.draw_pile.draw())
            
            for j in range(i+1, len(self.game_piles)):
                self.game_piles[j]["down"].append(self.draw_pile.draw())

    def determine_win_status(self):
        """Returns True if all suit_piles are complete, False otherwise"""
        for _, suit_pile in self.suit_piles.items():
            if len(suit_pile) != 13:
                return False
        return True
    
    def draw(self):
        """Executes a draw action. If the draw pile and discard piles are empty,
        informs the user that there are no more cards
        """
        if self.draw_pile.is_empty() and self.discard_pile.is_empty():
            print()
            print("ALERT: No more cards to draw")
            print()
        else:
            
            if self.draw_pile.is_empty():
                print("Draw pile empty. Shuffling discard pile.")
                self.discard_pile.shuffle()
                self.draw_pile = self.discard_pile
                self.discard_pile = Deck([])

            card = self.draw_pile.draw()
            self.players[0].add_to_hand(card)
            print()
            print(f"You have added a(n) {card} to your hand.")
            print()
            self.print_hand()

    def place_card(self):
        """Places a card from the user's hand to a relevant suit pile or game pile of choice"""
        
        player = self.players[0]

        self.print_sorted_suit_piles()
        print()
        self.print_game_piles()
        print()
        player.print_hand()
        print()

        s = "Please choose a card from your hand to place:"
        hand_choices = tuple(range(1, player.get_hand_len() + 1))
        card_choice = check_user_input(s, valid_resps=hand_choices, cast_type=int) - 1
        possible_locs = self._get_valid_placement_locs(player.get_card(card_choice))

        s = f"Please pick a pile you would like to move this card to:"
        to_pile_choice = check_user_input(s, valid_resps=tuple(range(1, len(possible_locs) + 1)), cast_type=int) - 1
        pile_choice = possible_locs[to_pile_choice]
        pile_choice.append(player.remove_card(card_choice))

        print()
        self.print_sorted_suit_piles()
        print()
        self.print_game_piles()
        print()
        player.print_hand()

    def move_pile(self):
        """Guides the user through a series of prompts to move a game pile to another
        game pile, possibly turning over facedown cards if the whole pile is moved
        """
        self.print_sorted_suit_piles()
        print()
        self.print_game_piles()
        print()

        # Get the "from" pile to move over
        valid_pile_choices = tuple(range(1, len(self.game_piles) + 1))
        s = f"Please pick a game pile you would like to move, using indices 1-{len(self.game_piles)}."
        while True:
            from_pile_choice = check_user_input(s, valid_resps=valid_pile_choices, cast_type=int) - 1
            from_up_pile = self.game_piles[from_pile_choice]["up"]
            if from_up_pile.is_empty():
                print("Error: No cards in this pile. Try again.")
            else:
                break
        
        # Get the desired top-level card in the "from" pile to move over
        if len(from_up_pile) == 1:
            from_highest_card_index = 0
        else:
            print()
            self.print_pile(from_pile_choice)
            print()
            s = f"Please pick the topmost card you want to move over, from 1 - {len(from_up_pile)}"
            t = tuple(i for i in range(1, len(from_up_pile) + 1))
            from_highest_card_index = check_user_input(s, valid_resps=t, cast_type=int) - 1
        
        possible_locs = self._get_valid_placement_locs(from_up_pile[from_highest_card_index])

        s = f"Please pick a possible location you would like to move this/these cards to."
        to_pile_choice = check_user_input(s, valid_resps=tuple(range(1, len(possible_locs) + 1)), cast_type=int) - 1
        pile_choice = possible_locs[to_pile_choice]
        pile_choice.extend(from_up_pile[from_highest_card_index:])
        for _ in range(from_highest_card_index, len(from_up_pile)):
            from_up_pile.pop()

        self._turn_over_card(from_pile_choice)
        
    def _get_valid_placement_locs(self, from_highest_card):
        
        print()
        print("Possible locations to place this card include:")
        possible_locs = []

        # Check suit piles
        card_suit = from_highest_card.get_suit()
        card_val = from_highest_card.get_value()
        suit_pile = self.suit_piles[card_suit.name]
        if (suit_pile.is_empty() and card_val is CardValue.ACE) or (not suit_pile.is_empty() and suit_pile[-1].get_value().value == card_val.value - 1):
            possible_locs.append(suit_pile)
            print(f"{len(possible_locs)}. {card_suit.name} suit pile: " + self._get_valid_loc_str(suit_pile))
        
        # Check game piles
        for i, pile in enumerate(self.game_piles):
            up_pile = pile["up"]
            down_pile = pile["down"]
            if card_val is CardValue.KING and up_pile.is_empty() and down_pile.is_empty():
                possible_locs.append(up_pile)
                print(f"{len(possible_locs)}. COLUMN {i + 1}: " + self._get_valid_loc_str(up_pile))
            elif not up_pile.is_empty():
                up_card = up_pile[-1]
                up_val = up_card.get_value().value
                if  card_val.value == up_val - 1 and from_highest_card.is_dif_color(up_card):
                    possible_locs.append(up_pile)
                    print(f"{len(possible_locs)}. COLUMN {i + 1}: " + self._get_valid_loc_str(up_pile))
        
        return possible_locs

    def _get_valid_loc_str(self, pile):
        if pile.is_empty():
            return "[]"
        else:
            return str(pile[-1])

    def _turn_over_card(self, pile_index):
        pile = self.game_piles[pile_index]
        if pile["up"].is_empty() and not pile["down"].is_empty():
            pile["up"].append(pile["down"].pop())

    def print_hand(self):
        self.players[0].print_hand()

    def print_game_piles(self):
        
        print("*************** PLAYABLE PILES ***************")

        print(self._separator_str.join(f"COLUMN {i + 1}".ljust(Card.get_pad_len()) for i in range(len(self.game_piles))))
        print(self._separator_str.join(f"".ljust(Card.get_pad_len()) for i in range(len(self.game_piles))))
        print(self._separator_str.join(f"{len(self.game_piles[i]['down'])} cards".ljust(Card.get_pad_len()) for i in range(len(self.game_piles))))
        print(self._separator_str.join(Card.get_empty_str() for _ in range(len(self.game_piles))))
        
        j = 0
        cont = True
        while cont:
            line = []
            cont = False
            for i in range(len(self.game_piles)):
                pile = self.game_piles[i]['up']
                if j < len(pile):
                    line.append(str(pile[j]))
                    cont = True
                else:
                    line.append(Card.get_empty_str())
            j += 1
            print(self._separator_str.join(line))

        print("*************** PLAYABLE PILES ***************")

    def print_pile(self, pile_index):
        print(f"***************     PILE {pile_index + 1}     ***************")
        for i, card in enumerate(self.game_piles[pile_index]["up"]):
            print(f"{i + 1}. {str(card)}")
        print(f"***************     PILE {pile_index + 1}     ***************")

    def print_sorted_suit_piles(self):
        
        print("***************   SUIT PILES   ***************")
        
        line = []
        for suit_name in sorted(self.suit_piles):
            line.append(suit_name.ljust(Card.get_pad_len()))
        print(self._separator_str.join(line))

        line = []
        for suit in sorted(self.suit_piles):
            pile = self.suit_piles[suit]
            if len(pile) > 0:        
                last_card = pile[-1]
                line.append(str(last_card))
            else:
                line.append(Card.get_empty_str())
        print(self._separator_str.join(line))
        
        print("***************   SUIT PILES   ***************")

def start_game():
    """The executable function that contains all game logic and user interaction"""
    
    print()
    input("Welcome to solitaire! Press Enter to continue.")
    print()
    print("Here is the initial game setup:")
    game = Solitaire(Player("Sam"))

    user_opts = tuple(range(1, 5))
    while True:
        
        win = game.determine_win_status()
        if win:
            print("Congratulations! You won!")
            break

        print()
        game.print_sorted_suit_piles()
        print()
        game.print_game_piles()
        print()
        game.print_hand()
        print()
        print("Choose from the following options:")
        print("1. Draw a card")
        print("2. Place a card")
        print("3. Move a pile")
        print("4. QUIT")
        
        choice = check_user_input("", valid_resps=user_opts, cast_type=int)
        print()

        match choice:
            case 1:
                game.draw()
            case 2:
                game.place_card()
            case 3:
                game.move_pile()
            case 4:
                break
        
    print("Thanks for playing. Goodbye!")

if __name__ == "__main__":
    start_game()
    