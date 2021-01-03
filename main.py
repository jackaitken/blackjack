suit = ["Hearts", "Diamonds", "Clubs", "Spades"]
color = ["Red", "Black"]
face = ["Jack", "Queen", "King", "Ace"]

class Card:
	def __init__(self, suit, color, number, face=None):
		self.suit = suit
		self.color = color
		self.number = number
		self.face = face

class Deck:
	def __init__(self):
		self.cards = []

deck = Deck()

# deal red
for i in range(0, 2):
	for j in range(1, 11):
		card = Card(suit[i], color[0], j)
		deck.cards.append((card.color, card.number, card.suit))
		
	for k in range(3):
		card = Card(suit[i], color[1], face[k])
		deck.cards.append((card.color, card.number, card.suit))

# deal black
for i in range(2, 4):
	for j in range(1, 11):
		card = Card(suit[i], color[1], j)
		deck.cards.append((card.color, card.number, card.suit))
	
	for k in range(3):
		card = Card(suit[i], color[1], face[k])
		deck.cards.append((card.color, card.number, card.suit))

