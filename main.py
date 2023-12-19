# import sys
# import os

# sys.path.append(os.path.dirname(os.path.realpath(__file__)))
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

        if choice == "1":
            slot_machine = SlotMachine()
            balance_change = slot_machine.play(balance)
            balance += balance_change
        elif choice == "6":  # '6' is the choice to quit
            break
        else:
            print("Invalid choice. Please try again.")

        print(f"Your balance is now: {balance}")
        if input("Play another game? (y/n): ").lower() != 'y':
            break

    print(f"You left the game with {balance}.")
    print("Thank you for playing!")

if __name__ == "__main__":
    main()