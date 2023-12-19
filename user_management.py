from common.config import MAX_LINES, MIN_BET, MAX_BET

def deposit():
    while True:
        amount = input("Enter the amount to deposit: $")

        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")

        else:
            print("Please enter a valid number.")
        
    return amount

def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")

        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print(f"Number of lines must be between 1 and {MAX_LINES}.")

        else:
            print("Please enter a valid number.")
        
    return lines

def get_bet():
    while True:
        amount = input("Enter the amount to bet: $")

        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between {MIN_BET} and {MAX_BET}.")

        else:
            print("Please enter a valid number.")
        
    return amount