from games.blackjack import Blackjack
from games.game import Game
from games.slots_machine import SlotMachine
from user_management import deposit


def select_game():
    print("Welcome to the Virtual Casino!")
    print("1. Slot Machine")
    print("2. Blackjack")
    print("3. Roulette")
    print("4. Poker")
    print("5. Craps")
    print("6. Quit")

    choice = input("Enter choice: ")
    return choice

def main():
    balance = deposit()
    while True:
        print(f"Your current balance is {balance}.")
        choice = select_game()

        game = None

        if choice == "1":
            game = SlotMachine()
        elif choice == "2":
            game = Blackjack()
        elif choice == "6":  # '6' is the choice to quit
            print(f"You left the game with {balance}.")
            print("Thank you for playing!")
            break
        else:
            print("Invalid choice. Please try again.")
            continue

        while True:
            balance_change = game.play(balance)
            balance += balance_change
            print(f"Your balance is now: {balance}")
            if balance <= 0:
                print("You've run out of money! Thanks for playing.")
                break
            
            replay_choice = input("Play the same game? (y/n): ").lower()
            if replay_choice != 'y':
                break

        print("Returning to the casino lobby...")


if __name__ == "__main__":
    main()