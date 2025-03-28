import random
from card import Card

class Deck:
    RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    
    def __init__(self):
        # Initialize a standard deck of 52 playing cards.
        self._cards = [Card(suit, rank) for suit in Deck.SUITS for rank in Deck.RANKS]
        
    def __str__(self):
        # Return a string representation of the deck.
        return f"Deck of {self.count} cards"
        
    @property
    def cards(self):
        # Get the list of cards in the deck.
        return self._cards
    
    @cards.setter
    def cards(self, new_cards):
        # Set the list of cards in the deck.
        for card in new_cards:
            if not isinstance(card, Card):
                raise ValueError(f"Invalid card: {card}. All elements in the deck must be intances of the Card class.")
        self._cards = new_cards
    
    @property
    def count(self):
        # Get the number of cards remaining in the deck.
        return len(self._cards)
    
    def shuffle(self):
        # Shuffle the deck of cards.
        random.shuffle(self._cards)
        
    def deal_one(self):
        # Deal one card from the deck.
        if not self._cards:
            raise ValueError("The deck is empty. Cannot deal a card.")
        return self._cards.pop(0)


