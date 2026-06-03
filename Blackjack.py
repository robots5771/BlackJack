from Player import Player
from Cards import Deck
import random as rand
class Blackjack (object):
    def __init__ (self):
        self.player1 = Player()
        self.BlackjackDeck = Deck()

        self.player1.playercards.append(rand.choice(self.BlackjackDeck.cards, k = 2))
        print(self.player1.playercards)


rungame = Blackjack()