from random import randint

suit = ["Hearts", "Diamonds", "Clubs", "Spades",]
color = ["Red", "Black"]
face = ["Jack", "Queen", "King", "Ace"]
deck = []

class Card:
	def __init__(self, suit, color, number, face=None):
		self.suit = suit
		self.color = color
		self.number = number
		self.face = face

for i in range(0, 2):
	for j in range(1, 11):
		card = Card(suit[i], color[0], j)
		deck.append((card.color, card.number, card.suit))
		print(f"{card.color} {card.number} of {card.suit}")

for i in range(2, 4):
	for j in range(1, 11):
		card = Card(suit[i], color[1], j)
		deck.append((card.color, card.number, card.suit))
		print(f"{card.color} {card.number} of {card.suit}")

