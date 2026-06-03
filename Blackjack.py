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

    def PlayerHitCards (self):
        print(f"Player : {self.player1.Current_Hand()}")
        print(f"Player : {self.Dealer1.Current_Hand()}")
        
        Disable = 0
        while Disable < 1 and self.player1.playercards != 21:
            AskPlayer = input("'hit' or 'stand'\n")
            if AskPlayer == "hit":
                PlayerCard = rand.choice(self.BlackjackDeck.cards)
                self.player1.Add_Card(PlayerCard)
                print(self.player1.Current_Hand())
                print(self.Dealer1.Current_Hand())
            else:
                Disable += 1
            
    def DealersTurn (self):
        if self.player1.Sum_Card() < 22:
            while self.Dealer1.Sum_Card() < 17:
                DealerCard = rand.choice(self.BlackjackDeck.cards)
                self.Dealer1.Add_Cards(DealerCard)
                if self.Dealer1.Sum_Card() > 17 or self.Dealer1.Sum_Card() > 21:  #This skips printing until the final dealer card is drawn to prevent spamming
                    print(self.player1.Current_Hand())
                    print(self.Dealer1.Current_Hand())
            
    
rungame = Blackjack()
rungame.PlayerHitCards()
rungame.DealersTurn()
