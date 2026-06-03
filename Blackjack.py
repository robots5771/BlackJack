from Player import Player
from Cards import Deck
from Dealer import Dealer
import random as rand

class Blackjack (object):
    def __init__ (self):
        self.player1 = Player()
        self.BlackjackDeck = Deck()
        self.Dealer1 = Dealer()

        Tally = 0
        while Tally < 2: 
            PlayerCard = rand.choice(self.BlackjackDeck.cards)
            DealerCard = rand.choice(self.BlackjackDeck.cards)
            self.player1.Add_Card(PlayerCard)
            self.Dealer1.Add_Cards(DealerCard)
            Tally += 1

    def HitCards (self):
        print(self.player1.playercards)
        print(self.Dealer1.DealerCards)
        
        Disable = 0
        while Disable < 1 and self.player1.Sum_Card() < 17:
            AskPlayer = input("'hit' or 'stand'\n")
            if AskPlayer == "hit":
                PlayerCard = rand.choice(self.BlackjackDeck.cards)
                self.player1.Add_Card(PlayerCard)
                print(self.player1.playercards)
                print(self.player1.Sum_Card())
            else:
                Disable += 1
            
    
rungame = Blackjack()
rungame.HitCards()
