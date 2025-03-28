Table of Contents

Overview
Features
How It Works
Setup

Overview

War is a simple card game often played by children. Each round, players reveal a card from their deck, and the player with the higher-ranking card wins the round. If the cards have the same rank, a "War" is declared, requiring a tie-breaker with additional cards. The goal is to win all the cards in the deck.

Features

Full implementation of the game's rules.
Randomized deck initialization and distribution.
Game loop to simulate rounds and resolve "Wars."
Customizable rules and settings for advanced gameplay.
Pair programming-friendly repository setup with clear issue tracking.
How It Works

Game Initialization:
A standard deck of 52 cards is shuffled and split evenly between two players
Gameplay:
Each player plays one card per round.
Higher-ranking card wins the round; the winner collects both cards.
In case of a tie, additional cards are played to determine the winner.
Win Condition:
In case of a tie, additional cards are played to determine the winner.
Setup:

Clone the repository: https://github.com/reganas/WarGame.git

Run the program: python war_game.py