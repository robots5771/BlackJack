class Dealer (object):
    def __init__ (self):
        self.DealerCards = []
    def Add_Cards(self, Card):
        self.DealerCards.append(Card)
    def Sum_Card(self):
        return sum(self.DealerCards)
    def Current_Hand(self):
        return (f"Dealer Cards : {self.DealerCards} ,  {self.Sum_Card()}")


 