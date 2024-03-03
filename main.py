# Golobal constant that sets Max Lines possible to 3
MAX_LINES = 3

# Global constant that sets Max bet possible to 100
MAX_BET = 100

#Global constant that sets Min bet possible to 1
MIN_BET = 1

# Function responsible for collecting user input that 
# gets the deposit from the user
def deposit():

    # While loop to continuely ask user to enter a deposit amount
    # until they give valid amount
    while True:
        
        # promit that is text that will happen before we allow user to start typing
        amount = input("What would you like to deposit? $")

        # Makes sure amount entered is actually a number
        if amount.isdigit():

            # Coverts string entered into a int
            amount = int(amount)

            # Checks if amount is greater than zero
            # If it is then function breaks out and returns amount
            if amount > 0:
                break
            else:

                # Prints if amount is less than zero to alert user
                print("Amount must be greater than 0.")
        else:

            # Prints if user does not enter a number
            print("PLease enter a number.")

    return amount

def get_number_of_lines():
    # While loop to continuely ask user to enter a deposit amount
    # until they give valid amount
    while True:
        
        # Promits the user to enter the number of lines to bet one 1 - 3 
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")

        # Makes sure amount entered is actually a number
        if lines.isdigit():

            # Coverts string entered into a int
            lines = int(lines)

            # Checks to see if amount of lines is greater than 1 but less than
            # Max Lines (3)
            if 1 <= lines <= MAX_LINES:
                break
            else:

                # Prints if bumber of lines is not between 1 - MAX_LINES (3)
                print("Enter a valid number of lines")
        else:

            # Prints if user does not enter a number
            print("PLease enter a number.")

    return lines

def get_bet():
    while True:
        
        # Promits the user to enter the number of lines to bet one 1 - 3 
        amount = input("What would you like to bet on each line? $")

        # Makes sure amount entered is actually a number
        if amount.isdigit():

            # Coverts string entered into a int
            amount = int(amount)

            # Checks to see if amount is greater than MIN_BET and less than 
            # MAX_BET
            if MIN_BET <= amount <= MAX_BET:
                break
            else:

                # Prints if amount is not between MIN_BET and MAX_BET
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}. ")
        else:

            # Prints if user does not enter a number
            print("PLease enter a number.")

    return amount

def main():
# Calling deposit function
    balance = deposit()
    lines = get_number_of_lines()
    bet = get_bet()

main()

