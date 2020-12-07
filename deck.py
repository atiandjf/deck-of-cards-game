import random


class Card(object):
    def __init__(self, suit, val):
        self.suit = suit
        self.value = val

    def show(self):

        print("{} of {}".format(self.value, self.suit))

# to avoid any possible errors comment al other classes else that Card and use followings:
#card = Card("Spades", 6)
#card.show()

class Deck(object):
    def __init__(self):
        # we gonna make an attribute called cards
        self.cards = []
        # we gonna build our deck of cards
        self.build()

    def build(self):
        for s in ["Spades", "Diamond", "Clubs", "Atia"]:
            for v in range (1, 14):
                self.cards.append(Card(s, v))

    def show(self):
        for c in self.cards:
            c.show()

    def shuffle(self):
        # we wanna go decremently from length of our cards to 0
        for i in range(len(self.cards)-1, 0, -1):
            #we want to make a random number to the left of our current position
            r = random.randint(0, i)
            # then we want to swipe two carts
            #???????????????? swipe
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def drawsCard(self):
        return self.cards.pop()

#{fruits = ['apple', 'banana', 'cherry']
#fruits.pop(1)
#print(fruits)}

#{fruits = ['apple', 'banana', 'cherry']
#x = fruits.pop(1)
#print(x)}


class Player(object):
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self, deck):
        # .append here specially add the drawn card to your hand
        self.hand.append(deck.drawsCard())

    def showHand(self):
        for card in self.hand:
            card.show()

    def discard(self):
        return self.hand.pop()





deck = Deck()

deck.shuffle()
#card.shuffle()
#card.show()

deck.drawsCard()
deck.show()

atia = Player("Atia")
atia.draw(deck)
atia.showHand()
#deck = Deck()
#deck.shuffle()
#deck.show()