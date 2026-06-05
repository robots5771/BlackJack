import random
class Deck(object):
    def __init__ (self):
        self.cards = [1,2,3,4,5,6,7,8,9,10,10,10,10,11]
    def Shuffle (self):
        random.shuffle(self.cards)