class Player (object):
    def __init__ (self):
        self.playercards = []
    def Add_Card (self, card):
        self.playercards.append(card)
    def Sum_Card(self):
        return sum(self.playercards)
    def Current_Hand(self):
        return (f"Player: {self.playercards} , {self.Sum_Card()}")