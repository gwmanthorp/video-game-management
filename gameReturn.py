# F322418
# 02/12/2023
'''
Asks the user for a game ID only
If the game ID matches one that has already been rented then it will return it
Uses the python datetime library to add an accurate return date
If invalid gameID, or game has not been rented, then an error will occur
'''

import feedbackManager as FM
import datetime
import database as db

def game_feedback(gameID, rating, comments):
    """
    Adds feedback for a game to the Game_Feedback.txt file.

    :param gameID: a string containing the inputted game ID
    :param rating: an integer containing the rating of the game returned
    :param comments: a string containing comments about the game returned
    """
    FM.add_feedback(gameID, rating, comments, "Game_Feedback.txt")

def main(gameID):
    """
    Main function to handle game return and feedback submission.
    Takes in game ID and outputs True or False depending on outcome

    :param gameID: a string containing the inputted game ID
    """
    date_time = datetime.datetime.now()
    date_time = date_time.strftime("%d/%m/%Y")

    rentals = db.database_access("Rental.txt")

    returned = False

    for record in rentals[1:]:
        # Check if the game ID matches one in rentals that has is unavailable
        if record[0] == gameID and record[2] == "":
            rentals[rentals.index(record)][2] = date_time
            returned = True

    if returned:
        db.return_game("Rental.txt", rentals)
        return True
    else:
        print("Game could not be returned")
        return False

def test_function():
    print("Testing:")
    # Test case 1: Test if inputted game ID is valid and has been rented out
    gameID = input("Enter a valid gameID that has been rented out: ")
    result1 = main(gameID)
    assert result1 == True, "Test Case 1 (main) Failed"

    # Test case 2: Test if inputted game ID is valid but is yet to be rented out
    gameID = input("Enter a valid gameID that has not been rented out: ")
    result2 = main(gameID)
    assert result2 == False, "Test Case 2 (main) Failed"

    # Test case 3: Test if inputted game ID is invalid
    result3 = main("INVALID GAME ID")
    assert result3 == False, "Test Case 3 (main) Failed"

#test_function()