from random import randint
import keyboard

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
		self.cards_remaining = 51

	def no_cards_left(self):
		return len(self.cards) == 0

	def card_dealt(self):
		self.cards_remaining -= 1

def main(deck):
	# deal red
	for i in range(0, 2):
		for j in range(2, 11):
			card = Card(suit[i], color[0], j)
			deck.cards.append(card)
			
		for k in range(4):
			card = Card(suit[i], color[1], None, face[k])
			deck.cards.append(card)

	# deal black
	for i in range(2, 4):
		for j in range(2, 11):
			card = Card(suit[i], color[1], j)
			deck.cards.append(card)
		
		for k in range(4):
			card = Card(suit[i], color[1], None, face[k])
			deck.cards.append(card)

	user_count = 0
	for i in range(len(deck.cards)):
		card = deck.cards[randint(0, deck.cards_remaining)]
		deck.cards.remove(card)
		deck.card_dealt()
		if card.face:
			user_count += 10
			print(f"{card.face} of {card.suit}")
			if user_count > 21:
				print(f"Oh no! {user_count}. You bust!")
				break
			elif user_count == 21:
				print("21! You win!")

		else:
			user_count += card.number
			print(f"{card.number} of {card.suit}")
			if user_count > 21:
				print(f"Oh no! {user_count}. You bust!")
				break
			elif user_count == 21:
				print("21! You win!")

		print(f"Type \"h\" to hit or \"s\" to stay", end="\n")

		user_input = input()

		if user_input == "h":
			continue

		else:
			print("Thanks for playing!")
			break


deck = Deck()
main(deck)