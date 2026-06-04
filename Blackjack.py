from Player import Player
from Cards import Deck
from Dealer import Dealer
import random as rand
import tkinter as tk
root = tk.Tk() #The Window Label Is Contained In
root.title("Blackjack Simulation")
root.geometry("350x165")


class Blackjack(object):
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
        print(self.player1.Current_Hand())
        print(self.Dealer1.Current_Hand())

    def PlayerHitCards(self):

            if self.player1.Sum_Card() < 21:
                PlayerCard = rand.choice(self.BlackjackDeck.cards)
                self.player1.Add_Card(PlayerCard)
                print(self.player1.Current_Hand())
                print(self.Dealer1.Current_Hand())

            if self.player1.Sum_Card() > 21:
                labelPlayer.config(state = "disabled")
                labelDealer.config(state = "disabled")
                Deals.config(state = "disabled")
                Stand.config(state = "disabled")
            elif self.player1.Sum_Card() == 21:
                labelPlayer.config(state = "disabled")
                labelDealer.config(state = "disabled")
                Deals.config(state = "disabled")
                Stand.config(state = "disabled")
                DealersTurnAndWinOrLose()
            
        
    def DealersTurn (self):
        while self.Dealer1.Sum_Card() < 17 and self.player1.Sum_Card() < 22:
            if self.player1.Sum_Card() < 22:
                DealerCard = rand.choice(self.BlackjackDeck.cards)
                self.Dealer1.Add_Cards(DealerCard)
                if self.Dealer1.Sum_Card() > 17 or self.Dealer1.Sum_Card() > 21:  #This skips printing until the final dealer card is drawn to prevent spamming
                    print(self.player1.Current_Hand())
                    print(self.Dealer1.Current_Hand())
                    print()
                else:
                    print(self.player1.Current_Hand())
                    print(self.Dealer1.Current_Hand())
                    print()


    def WinLoseBust(self):
        if self.player1.Sum_Card() > 21:
            print("Bust")
            OutCome.config(text = "Bust")
        elif self.player1.Sum_Card() > self.Dealer1.Sum_Card():
            print("Win")
            OutCome.config(text = "Win")
        elif self.player1.Sum_Card() == 21 and self.Dealer1.Sum_Card() < 21:
            print("Win")
            OutCome.config(text = "Win")
        elif self.player1.Sum_Card() == 21 and self.Dealer1.Sum_Card() > 21:
            print("Win")
            OutCome.config(text = "Win")
        elif self.player1.Sum_Card() == self.Dealer1.Sum_Card():
            print("Push")
            OutCome.config(text = "Push")
        else:
            print("Lose")
            OutCome.config(text = "Lose")
            


rungame = Blackjack()


def PlayerHits():
    rungame.PlayerHitCards()
    labelPlayer.config(text = rungame.player1.Current_Hand())

def DealersTurnAndWinOrLose():
    labelPlayer.config(state = "disabled")
    labelDealer.config(state = "disabled")
    Deals.config(state = "disabled")
    Stand.config(state = "disabled")
    rungame.DealersTurn()
    rungame.WinLoseBust()
    labelDealer.config(text = rungame.Dealer1.Current_Hand())


    
    

labelPlayer = tk.Label(root, text= rungame.player1.Current_Hand()) #Label Controls
labelPlayer.pack() #Place Label Inside Window

labelDealer = tk.Label(root, text= rungame.Dealer1.Current_Hand()) #Label Controls
labelDealer.pack() #Place Label Inside Window

Cards = tk.Label(root, text= f"Cards: {rungame.BlackjackDeck.cards}") #Label Controls
Cards.pack() #Place Label Inside Window

OutCome = tk.Label(root, text= f"Outcome Unknown") #Label Controls
OutCome.pack() #Place Label Inside Window

Deals = tk.Button(root, text="Deal", width = 25, command = PlayerHits)
Deals.pack()

Stand = tk.Button(root, text="Stand", width = 25, command = DealersTurnAndWinOrLose)
Stand.pack()






root.mainloop()

