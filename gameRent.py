# F322418
# 30/11/2023
'''
Asks the user for a game ID and customer ID
Checks if customer ID is valid/subscription is valid, or hasn't reached max rentals
Checks if gameID is valid/hasn't already been rented out
Then if this is the case it will rent the game to the customer
'''
import subscriptionManager as SM
import datetime
import database as db

subscriptions = SM.load_subscriptions("Subscription_Info.txt")

def rental_limit(customerID, rentals):
    """
    Calculate the number of available game rentals for a customer
    Takes in customerID and rentals list
    Returns the number of available game rents

    :param cusomterID: a string containing the inputted customer ID
    :param rentals: a list of the game rentals that have been made
    """
    gameCount = 0

    # Iterates through the rentals list, checks if the customer has rented a game
    for data in rentals[1:]:
        if data[3] == customerID and data[2] == "":
            gameCount += 1

    # Calculates the amount of available rents left
    availableRents = SM.get_rental_limit(subscriptions[customerID]["SubscriptionType"]) - gameCount
    return availableRents

def game_availability(gameIdInput, rentals):
    """
    Check if a game is available for rent.
    Either returns True or outputs an error message, either:
    - Tells user the game they inputted is already rented out
    - Tells user that the game ID they entered was invalid

    Takes in the game ID and rentals list and outputs True or False

    :param gameIdInput: a string containing the inputted game ID
    :param rentals: a list of the game rentals that have been made
    """

    for data in rentals[1:]:
        # Checks gameID is already in rentals list, and it has no return date
        if gameIdInput == data[0] and data[2] == "":
            print("Game is already rented out")
            return False

    games = db.database_access("Game_Info.txt")

    # Checks inputted gameID is in the "Game_Info.txt" and not a made-up one
    for data in games[1:]:
        if data[0] == gameIdInput:
            return True

    print("Invalid game ID entered")
    return False

def main(customerIdInput, gameIdInput):
    """
    Main function to handle the game rental process
    Runs through and makes necessary checks for each possible scenario
    Takes in gam ID and customer ID, returns True or False accordingly

    :param customerIdInput: a string containing the inputted customer ID
    :param gameIdInput: a string containing the inputted game ID
    """
    rentals = db.database_access("Rental.txt")

    date_time = datetime.datetime.now()
    date_time = date_time.strftime("%d/%m/%Y")

    for customerID in subscriptions:
        if customerID == customerIdInput:
            if SM.check_subscription(customerID, subscriptions):
                # Checks customer has any rents left and if game is available
                limit = rental_limit(customerID, rentals)
                if limit > 0:
                    if game_availability(gameIdInput, rentals):
                        recordToAdd = [gameIdInput, date_time, "", customerID]
                        db.add_record("Rental.txt", recordToAdd)
                        print(gameIdInput + " has been rented to " + customerIdInput)
                        return True
                    else:
                        return False
                else:
                    print("Game renting limit met")
                    return False
            else:
                print("Customer's subscription is inactive")
                return False
    print("Invalid customer ID entered")
    return False

def test_function():
    print("Testing:")
    # Tests rental limit for a customer with an active subscription
    customerID=input("\nEnter a customer ID that has an active subscription: ")
    gameID=input("Enter a valid gameID that has not been rented out: ")
    result1=main(customerID, gameID)
    assert result1 == True, "Test Case 1 (main) Failed"

    # Tests if game has already been rented out
    customerID=input("\nEnter a customer ID that has an active subscription: ")
    gameID=input("Enter a gameID that has already been rented out: ")
    result2=main(customerID, gameID)
    assert result2 == False, "Test Case 2 (main) Failed"

    # Tests if invalid customerID is inputted
    customerID=input("\nEnter an invalid customerID: ")
    gameID=input("Enter a valid gameID that has not been rented out: ")
    result3 = main(customerID, gameID)
    assert result3 == False, "Test Case 3 (main) Failed"

    # Tests if invalid gameID is inputted
    customerID =input("\nEnter a customer ID that has an active subscription: ")
    gameID = input("Enter an invalid gameID: ")
    result4 = main(customerID, gameID)
    assert result4 == False, "Test Case 4 (main) Failed"

    # Tests if inactive subscription customer ID is inputted
    customerID=input("\nEnter a customer ID that has an inactive subscription:")
    gameID=input("Enter a valid gameID that has not been rented out: ")
    result5 = main(customerID, gameID)
    assert result5 == False, "Test Case 5 (main) Failed"

    # Tests if both invalid customerID and gameID are inputted
    customerID = input("\nEnter an invalid customerID: ")
    gameID = input("Enter an invalid gameID: ")
    result6 = main(customerID, gameID)
    assert result6 == False, "Test Case 6 (main) Failed"

#test_function()