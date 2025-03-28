class Card:
    def __init__(self, suit, rank):
        """
        Initialize a card with a suit and rank.
        :param suit: The suit of the card (e.g., 'Hearts', 'Diamonds', 'Clubs', 'Spades').
        :param rank: The rank of the card (e.g., '2', '3', ..., 'King', 'Ace').
        """
        if suit not in ['Hearts', 'Diamonds', 'Clubs', 'Spades']:
            raise ValueError("Invalid suit. Must be 'Hearts', 'Diamonds', 'Clubs', or 'Spades'.")
        if rank not in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']:
            raise ValueError("Invalid rank. Must be one of '2', '3', ..., 'King', 'Ace'.")
        self._suit = suit
        self._rank = rank
        
    @property
    def suit(self):
        """
        Get the suit of the card.
        :return: The suit of the card.
        """
        return self._suit
    
    @suit.setter
    def suit(self, value):
        if value not in ['Hearts', 'Diamonds', 'Clubs', 'Spades']:
            raise ValueError("Invalid suit. Must be 'Hearts', 'Diamonds', 'Clubs', or 'Spades'.")
        self._suit = value
        
    @property
    def rank(self):
        return self._rank
        
    @rank.setter
    def rank(self, value):
        valid_ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        if value not in valid_ranks:
            raise ValueError(f"Invalid rank. Must be one of {valid_ranks}.")
        self._rank = value
        
    def __str__(self):
        """
        Return a string representation of the card.
        :return: A string in the format 'Rank of Suit' (e.g., 'Ace of Hearts').
        """
        return f"{self.rank} of {self.suit}"

    def __repr__(self):
        """
        Return a string representation for debugging.
        :return: A string in the format 'Card(rank, suit)'.
        """
        return f"Card('{self.rank}', '{self.suit}')"