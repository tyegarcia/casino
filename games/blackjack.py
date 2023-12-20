from games.game import Game
import random
from common.config import MIN_BET, MAX_BET, DECK, CARD_VALUES
from user_management import get_bet

class Blackjack(Game):
    def __init__(self):
        super().__init__("Blackjack")

    def play(self, balance):
        self.balance = balance
        return self.play_blackjack()
    
    def play_blackjack(self):
        while True:
            bet = get_bet()
            if bet > self.balance:
                print(f"You do not have enough money to make that bet. Your current balance is {self.balance}.")
                continue
            print(f"You are betting {bet}.")
            break

        deck = self.create_deck()
        self.shuffle_deck(deck)
        players_hands, dealer_hand = self.deal_cards(deck, 1)
        print(f"Your hand: {players_hands[0]}, Dealer's hand: [{dealer_hand[0]}, Hidden]")

        if self.get_hand_value(players_hands[0]) == 21:
            if self.get_hand_value(dealer_hand) == 21:
                print("Both you and the dealer have blackjack! It's a push.")
                return 0
            else:
                print("You have blackjack! You win!")
                self.balance += bet * 2
                return bet * 2

        player_result = self.player_turn(players_hands[0], deck)
        if player_result == "bust":
            self.balance -= bet
            print(f"You busted! New balance: {self.balance}")
            return -bet

        print(f"Dealer's hand: {dealer_hand}")
        dealer_result = self.dealer_turn(dealer_hand, deck)
        print(f"Dealer's final hand: {dealer_hand}")

        outcome = self.determine_outcome(players_hands[0], dealer_hand)
        if outcome == "win":
            self.balance += bet * 2
            print(f"You win! New balance: {self.balance}")
            return bet * 2
        elif outcome == "loss":
            self.balance -= bet
            print(f"You lose! New balance: {self.balance}")
            return -bet
        else:
            print(f"It's a push! Balance remains the same: {self.balance}")
            return 0

    @staticmethod
    def create_deck():
        deck = []
        for card, count in DECK.items():
            deck.extend([card] * count)
        return deck
    
    @staticmethod
    def shuffle_deck(deck):
        random.shuffle(deck)

    @staticmethod
    def deal_cards(deck, num_players):
        players_hands = {player: [] for player in range(num_players)}
        dealer_hand = []

        for _ in range(2):
            for player in range(num_players):
                players_hands[player].append(deck.pop())
            dealer_hand.append(deck.pop())

        return players_hands, dealer_hand

    def player_turn(self, player_hand, deck):
        while True:
            print(f"Your hand is: {player_hand}")
            print(f"Your hand value is: {self.get_hand_value(player_hand)}")
            if self.get_hand_value(player_hand) > 21:
                print("You busted!")
                return "bust"

            if input("Hit or stand? (h/s): ").lower() == 'h':
                player_hand.append(deck.pop())
            else:
                return "stand"

    def get_hand_value(self, hand):
        total_value = 0
        ace_count = 0
        for card in hand:
            if card == "A":
                ace_count += 1
            else:
                total_value += CARD_VALUES[card]

        for _ in range(ace_count):
            if total_value + 11 <= 21:
                total_value += 11
            else:
                total_value += 1

        return total_value

    def dealer_turn(self, dealer_hand, deck):
        while self.get_hand_value(dealer_hand) < 17:
            dealer_hand.append(deck.pop())
            print(f"Dealer hand is: {dealer_hand}")
            print(f"Dealer hand value is: {self.get_hand_value(dealer_hand)}")
            if self.get_hand_value(dealer_hand) > 21:
                print("Dealer busted!")
                return "bust"
        return "stand"

    def determine_outcome(self, player_hand, dealer_hand):
        player_value = self.get_hand_value(player_hand)
        dealer_value = self.get_hand_value(dealer_hand)

        if player_value > 21:
            return "loss"
        elif dealer_value > 21 or player_value > dealer_value:
            return "win"
        elif player_value == dealer_value:
            return "push"
        else:
            return "loss"



