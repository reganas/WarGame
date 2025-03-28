from typing import List, Union
from card import Card

class Player:
    def __init__(self, name):
        self._name = name
        self._cards = []
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Name must be a non-empty string.")
        self._name = value
        
    @property
    def cards(self):
        return self._cards
    
    @property
    def card_count(self):
        return len(self._cards)
    
    def add_cards(self, new_cards: Union[Card, List[Card]]) -> None:
        # Add cards to the player's hand.
        # param new_cards: A single card or a list of cards to add.
        if isinstance(new_cards, list):
            self._cards.extend(new_cards)
        else:
            self._cards.append(new_cards)
            
    def play_card(self) -> Union[Card, None]:
        # Play the top card from the player's pile.
        # return: The top card, none in the pile is empty
        if not self._cards:
            raise ValueError(f"{self.name} has no cards left to play.")
        return self._cards.pop(0)
    
    def __str__(self):
        # Return a string representation of the player.
        # return: the player's name and his cards
        return f"{self.name} has {self.card_count} cards"
        
    def __repr__(self):
        # Return a string representation for debugging.
        # return: the player's name and his cards
        return f"Player('{self.name}', {self.card_count} cards)"

    