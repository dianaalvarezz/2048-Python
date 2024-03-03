# Golobal constant that sets Max Lines possible to 3
MAX_LINES = 3

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
        
        # 
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")

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


def main():
# Calling deposit function
    balance = deposit()

main()

