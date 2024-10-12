import random

MIN_BET=1
MAX_BET=1000
MAX_LINES = 3
ROWS = 3
COLS = 3

# dictionary
symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8,
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2,
}

def deposit():
    while True:
      amount = input("how much would you like to deposit?")
      if amount.isdigit():
          amount = int(amount);
          if amount > 0: break
          else: print("amount must be greater than zero")
      else: print("please enter a number")
    return amount

def get_number_of_lines():
    while True:
      lines = input("enter the number of the lines to bet on (1-" + str(MAX_LINES) + "?")
      if lines.isdigit():
          lines = int(lines);
          if 1 <= lines <= MAX_LINES: break
          else: print("enter a valid number")
      else: print("please enter a number")
    return lines

def get_bet():
    while True:
        bet = input("how much would you like to bet? $")
        if bet.isdigit():
            bet = int(bet);
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"amount must be between ${MIN_BET} and ${MAX_BET}")
        else:
            print("please enter a number")
    return bet

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for i in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        # copy all symbols without reference
        curr_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(curr_symbols)
            curr_symbols.remove(value)
            column.append(value)

        columns.append(column)
    return columns

def print_slot_machine_spin(cols):
    for row in range(len(cols[0])):
        for i, col in enumerate(cols):
            if i != len(cols) - 1:
                print(col[row], end="|")
            else:
                print(col[row], end="")
        print()

def check_winning(cols, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = cols[0][line]
        for col in cols:
            symbol_to_check = col[line]
            if symbol != symbol_to_check:
                break
            else:
                winnings += values[symbol] * bet
                winning_lines.append(lines + 1)

    return winnings, winning_lines


def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"you don't have enough money, your current balance is ${balance}")
            return

    print(f"you are betting ${bet} on ${lines} lines. total bet is equal to ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine_spin(slots)
    winnings, winning_lines = check_winning(slots, lines, bet, symbol_value)

    print(f"you have won ${winnings}")
    print(f"you have won on lines: ", *winning_lines)

    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"your balance is ${balance}")
        value = input("Press enter to play (q to quit).")
        if value == 'q':
            break
        balance += spin(balance)
    print(f"you have won ${balance}")

main()