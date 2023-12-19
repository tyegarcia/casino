import random
from common.utilities import print_slot_machine_spin
from games.game import Game
from user_management import get_bet, get_number_of_lines

class SlotMachine(Game):
    # Constants
    ROWS = 3
    COLS = 3

    symbol_count = {
        "7": 3,
        "BAR": 3,
        "BELL": 3,
        "PLUM": 6,
        "ORANGE": 6,
        "CHERRY": 6,
        "LEMON": 6
    }

    symbol_value = {
        "7": 100,
        "BAR": 50,
        "BELL": 20,
        "PLUM": 14,
        "ORANGE": 10,
        "CHERRY": 7,
        "LEMON": 4
    }

    def __init__(self):
        super().__init__("Slot Machine")

    def play(self, balance):
        self.balance = balance
        return self.spin()

    def spin(self):
        lines = get_number_of_lines()
        while True:
            bet = get_bet()
            total_bet = bet * lines

            if total_bet > self.balance:
                print(f"You do not have enough money to make that bet. Your current balance is {self.balance}.")
                continue

            print(f"You are betting {bet} on {lines} lines. Total bet is {total_bet}.")
            break

        slots = self.get_slot_machine_spin()  # Corrected call
        print_slot_machine_spin(slots)
        winnings, winning_lines = self.check_winnings(slots, lines, bet)
        print(f"You won {winnings}!")
        print(f"You won on lines: ", *winning_lines)
        return winnings - total_bet
    
    def check_winnings(self, columns, lines, bet):
        winnings = 0
        winning_lines = []
        for line in range(lines):
            symbol = columns[0][line]
            for column in columns:
                symbol_to_check = column[line]
                if symbol != symbol_to_check:
                    break
            else:
                winnings += self.symbol_value[symbol] * bet
                winning_lines.append(line + 1)

        return winnings, winning_lines

    def get_slot_machine_spin(self):
        all_symbols = []
        for symbol, count in self.symbol_count.items():
            all_symbols.extend([symbol] * count)

        columns = []
        for _ in range(self.COLS):
            column = []
            current_symbols = all_symbols[:]
            for _ in range(self.ROWS):
                value = random.choice(current_symbols)
                current_symbols.remove(value)
                column.append(value)
            
            columns.append(column)
        
        return columns
