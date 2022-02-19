from random import *


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def random_card(player_array, card_numbers):            #Choice random card/ cards sum
	for i in range(0, card_numbers):
		player_array.append(choice(cards))
	return player_array


def check_winner(player_cards, dealer_cards, more_card = 0):
	if more_card == 1:
		random_card(player_cards, 1)
		player_card_sum = sum(player_cards)
		dealer_card_sum = sum(dealer_cards)
		print(f"--You ask for a card.\n----Your cards: {player_cards}")
		if dealer_card_sum < 17 and not player_card_sum > 21:
			random_card(dealer_cards, 1)
			dealer_card_sum = sum(dealer_cards)
			print(f"--Dealer take a card.")

	else:
		player_card_sum = sum(player_cards)
		dealer_card_sum = sum(dealer_cards)

	def check(player_card_sum, dealer_card_sum):
		if player_card_sum == 21:
			if dealer_card_sum != 21:
				print("You Win!")
		elif player_card_sum > 21:
			if 11 in player_cards:
				player_card_sum -= 10
				print("You: 11 - 1")
				check(player_card_sum, dealer_card_sum)
			else:
				print("You Loose!")
		elif dealer_card_sum > 21:
			if 11 in dealer_cards:
				dealer_card_sum -= 10
				print("Dealer: 11 - 1")
				check(player_card_sum, dealer_card_sum)
			else:
				print("You Win!")
		elif player_card_sum > dealer_card_sum:
			print("You Win!")
		elif player_card_sum < dealer_card_sum and not dealer_card_sum > 21:
			print("You Loose!")
		elif dealer_card_sum > 21 and not player_card_sum > 21:
			print("You Win!")
		elif dealer_card_sum > 21 and player_card_sum > 21:
			print("Nobody Win!")
		elif player_card_sum == dealer_card_sum:
			print("Draw!")
		else:
			print("Error!")

	print(f"----Dealer cards: {dealer_cards}")
	check(player_card_sum, dealer_card_sum)


def start_game():
	dealer_pairs = []                          			#Dealer cards array, empty
	your_pairs = []							   			#Your cards array, empty
	random_card(dealer_pairs, 2)			   			#Random choise of 2 cards for dealer
	random_card(your_pairs, 2)				  			#Random choise of 2 cards for you

	print(f"Dealer cards: [{dealer_pairs[0]}, ?]\nYour cards: {your_pairs}")

	next = input("Your decision: 'card' or 'open'? ")
	if next == "card":
		check_winner(your_pairs, dealer_pairs, 1)
	elif next == "open":
		print(f"----Your cards: {your_pairs}")
		check_winner(your_pairs, dealer_pairs)

	restart = input("\nRepeat game? 'y' or 'n' :  ")
	if restart == "y":
		print("______________________________________________________________\n")
		start_game()
	else:
		print("Good bye!")



start_game()