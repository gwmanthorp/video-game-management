# F322418
# 26/11/2023
'''
Uses search terms of title, genre and platform as an input
Returns all related games which match to the inputted search data
'''
import database as db

def game_search(searchTerm):
    '''
    Searches for games in the database based on the provided search term
    Takes in a search term and then returns a list of items related to that term

    :param searchTerm: a string containing the inputted search term
    :return: list of games related to the inputted search term
    '''
    database = db.database_access("Game_Info.txt")
    relatedItems = []

    for record in database[1:]:
        # If the search term is in any relevant field (title, genre, platform)
        if searchTerm in record[1].lower() or searchTerm in record[2].lower() or searchTerm in record[3].lower():
            relatedItems.append(record)
            continue

    return relatedItems

def main(searchTerm):
    '''
    Main function to search for and display available and unavailable games
    Takes in a search term and returns the available and unavailable lists

    :param searchTerm: a string containing the inputted search term
    :return availableString: a string containing available games
    :return unavailableString: a string containing unavailable games
    '''
    relatedItems = game_search(searchTerm.lower())

    available = []
    unavailable = []

    rentals = db.database_access("Rental.txt")

    # Iterates through rentals, checks if gameID matches in relatedItems
    for i in rentals:
        for j in relatedItems:
            # If match is found and game is not available, mark it unavailable
            if i[0] == j[0] and i[2] == "" and j not in unavailable:
                unavailable.append(j)

    # Separates unavailable games from available ones
    for each in relatedItems:
        if each not in unavailable:
            available.append(each)

    # Outputs available and unavailable games
    if len(available)>0:
        availableString = "Available\n"
        for each in available:
            availableString += str(each)+"\n"
    else:
        availableString = "No available games matching this criteria"
    if len(unavailable)>0:
        unavailableString = "\nUnavailable\n"
        for each in unavailable:
            unavailableString += str(each)+"\n"
    else:
        unavailableString = "\nNo unavailable games matching this criteria"
    return availableString, unavailableString

def test_function():
    print("Testing:")
    # Tests for a known game title
    result1 = game_search("minecraft")
    assert len(result1) != 0, "Test case 1 failed"

    # Tests for a game genre
    result2 = game_search("action")
    assert len(result2)!=  0, "Test case 2 failed"

    # Tests for a game platform
    result3 = game_search("xbox")
    assert len(result3) != 0, "Test case 3 failed"

    # Tests if the game entered doesn't exist
    result4 = game_search("Nonexistent Game")
    assert len(result4) == 0, "Test case 4 failed"

#test_function()