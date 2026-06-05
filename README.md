# Blackjack Simulation

## Overview

This is an ongoing project of mine where i am demonstrating skills along the way.

## Current Features

### Gameplay

- Deal two starting cards to play
- Deal two starting cards to dealer
- Dealers second card is hidden
- Player Decisions: "Hit" or "Stand"
- Upon Standing under 21 the dealer will begin drawing themselves cards until they hit 17
- If the dealer goes over 21 they bust
- If the player goes over 21 the player busts
- Restart Game Capability

### OOP

- Card Class , Handles card deck creation + Shuffling
- Player Class and Dealer Class handles card creation + AddCard() + Sum_Card() + CurrentHand()
- Blackjack Class , Handles main game flow + Tkinter Logic
- Individial Scripts used to break down code into more followable parts

### How Cards Are Managed

- Player Card + Dealer Cards are stored in lists
- Classes continuely sum card totals for both the dealer and player
- Python Random Module used for card generation from the deck
- Deck Shuffles after each card

### Graphical User Interface

- Pythons built in Tkinter Module Used
- Buttons , Labels used for interactivity and user feedback 
- Player and Dealer totals shown continusly
- Buttons disable upon game end 

## Current Technologies Applied In This Project

- Python
- Tkinter
- Random Module

## Future Features

- Real Card Deck Implementation
- Ace Handling
- Credits system for simulated betting
