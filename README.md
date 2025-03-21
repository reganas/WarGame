# WarGame
Pair Programming task

Game Requirements:

1. Players
The game typically has two players.

2. Deck Setup
Use a standard 52-card deck, where each card has:

A rank (e.g., 2-10, J, Q, K, A).

A suit (e.g., hearts, diamonds, clubs, spades).

Cards should have a value assigned to ranks for comparison purposes (e.g., Ace = highest).

3. Dealing the Cards
Shuffle the deck and deal cards evenly to both players. Each player starts with their own pile of cards.

4. Gameplay
The game is played in rounds:

Both players draw the top card from their piles.

Compare the values of the two cards:

Higher value wins: The player with the higher card takes both cards and places them at the bottom of their pile.

Tie (war): If both cards have the same value:

Each player places three cards face-down and one card face-up (if they have enough cards). The face-up cards are compared.

The winner of the war takes all the cards.

If there's another tie, repeat the process until there’s a winner or a player runs out of cards.

Players continue drawing cards until one player runs out of cards, losing the game.

5. Winning the Game
The game ends when one player has all the cards or another termination condition (like a maximum number of rounds).
