import random

class Card(object):
    suits = ['hearts', 'diamonds', 'spades', 'clubs']
    rank = [None, 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack',
            'Queen', 'King']

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def getRank(self):
        return self.rank

    def getSuit(self):
        return self.suit

    def __str__(self):
        return "{0} of {1}".format(Card.rank[self.rank], Card.suits[self.suit])


class Deck(object):
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(rank, suit)
                self.cards.append(card)

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)

    def shuffle(self):
        random.shuffle(self.cards)



if __name__ == '__main__':
    deck = Deck()
    deck.shuffle()
    print(deck)
