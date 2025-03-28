from deck import Deck
from player import Player
from card import Card
from typing import List, Optional

def play_round(player1: Player, player2: Player) -> None:
    # Play a single round of the game
    card1 = player1.play_card()
    card2 = player2.play_card()
    
    print(f"{player1.name} plays {card1}")
    print(f"{player2.name} plays {card2}")
    
    # Compare the cards 
    if Deck.RANKS.index(card1.rank) > Deck.RANKS.index(card2.rank):
        print(f"{player1.name} wins the round!")
        player1.add_cards([card1, card2])
    elif Deck.RANKS.index(card1.rank) < Deck.RANKS.index(card2.rank):
        print(f"{player2.name} wins the round!")
        player2.add_cards([card1, card2])
    else:
        print("It's a tie! We are at war!")
        handle_war(player1, player2, [card1, card2])
        
def handle_war(player1: Player, player2: Player, war_pile: List[Card], max_recursion: int = 3) -> None:
    
    if max_recursion == 0:
        print("Too many ties! Ending the game.")
    
    # Handle the war scenario when two cards have the same rank
    if player1.card_count < 4:
        print(f"{player1.name} does not have enough cards for war. {player2.name} wins the game!")
        return
    elif player2.card_count < 4:
        print(f"{player2.name} does not have enough cards for war. {player1.name} wins the game!")
        return
    
    for _ in range(3):
        if player1.card_count > 0:
            war_pile.append(player1.play_card())
        if player2.card_count > 0:
            war_pile.append(player2.play_card())
            
    # Each player plays another card face down and one card face up
    card1 = player1.play_card()
    card2 = player2.play_card()
    war_pile.extend([card1, card2])
    
    print(f"{player1.name} plays {card1}")
    print(f"{player2.name} plays {card2}")
    
    # Compare the cards again
    if Deck.RANKS.index(card1.rank) > Deck.RANKS.index(card2.rank):
        print(f"{player1.name} wins the war!")
        player1.add_cards(war_pile)
    elif Deck.RANKS.index(card1.rank) < Deck.RANKS.index(card2.rank):
        print(f"{player2.name} wins the war!")
        player2.add_cards(war_pile)
    else:
        print("It's a tie! We are at war!")
        handle_war(player1, player2, war_pile, max_recursion - 1)
        
def check_win_condition(player1: Player, player2: Player) -> Optional[str]:
    # Check if the player has won the game
    if player1.card_count == 0:
        return player2.name
    elif player2.card_count == 0:
        return player1.name
    else:
        return None
        