# F322418
# 03/12/2023
'''
This module outputs to the user a list of games that could be removed
This is based on the rental frequency of each game
Using this data a bar chart is displayed which displays the rental frequency of each game
It also displays games that received low ratings
User enters a limit rating, and it displays all games that received lower than that rating
Also displays how many times it received a rating lower as well as the comments
'''

import matplotlib.pyplot as plt
import database as db

def get_games(database):
    """
    Extracts the names of games from the given database
    Takes in the database as a parameter and returns the list of games

    :param database: a list containing contents of "Game_Info.txt"
    :return games: a list containing only the gameID of each game
    """
    games = []

    # Excludes the first element in the database
    for data in database[1:]:
        games.append(data[0])

    return games


def main(n):
    """
    Main function to analyze and visualize game rentals
    Gathers necessary data and outputs a bar chart of game rental frequency

    :param n: an integer containing the max ratings value that is checked by the function

    """
    rentalsDatabase = db.database_access("Rental.txt")
    gameDatabase = db.database_access("Game_Info.txt")

    games = get_games(gameDatabase)
    rentedGames = get_games(rentalsDatabase)

    gamesAndRents = [[], []]

    for i in range(len(games) - 1):
        gamesAndRents[0].append(games[i])
        gamesAndRents[1].append(rentedGames.count(games[i]))

    frequency_evaluation(gamesAndRents)
    plot_function(gamesAndRents[0], gamesAndRents[1], "Rentals", "Games",
                  "Game Rentals")
    rGame = feedback_evaulation(n)
    plot_function(rGame[0], rGame[1], "Number of sub "+str(n)+" ratings", "Games", "Low Ratings Count")

def plot_function(x, y, x_label, y_label, title):
    '''
    Takes in x and y data and creates a graph with labels that are parameters
    Uses matplotlib to plot this graph, uses the title parameter to name it

    :param x: a list containing the data for the x-axis of the chart
    :param y: a list containing the data for the y-axis of the chart
    :param x-label: a string containing the label for the x-axis of the chart
    :param y-label: a string containing the label for the y-axis of the chart
    :param title: a string containing the title for the top of the chart
    '''
    # Create and display a bar chart using frequency of each game ID
    fig, ax = plt.subplots()
    xticks = range(min(y), max(y) + 1)
    ax.set_xticks(xticks)
    # Plot a horizontal bar chart using frequency of each game ID
    plt.barh(x, y)
    # Adjust the layout for better visualization
    plt.subplots_adjust(left=0.24)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.show()

def frequency_evaluation(gamesAndRents):
    """
    Evaluate game rentals, and identify games that could be removed
    Based on the rental frequencies of all games
    Then these games are outputted

    :param gamesAndRents: a list containing both the games and rental frequency
    """

    removableGames = []

    # Finds the lowest game rental frequency
    lowest = gamesAndRents[1][0]
    for i in range(len(gamesAndRents[0])):
        # If lower "lowest" found then set that as new lowest
        if gamesAndRents[1][i] < lowest:
            lowest = gamesAndRents[1][i]
    # If game matches lowest, add to removable games
    for i in range(len(gamesAndRents[0])):
        if gamesAndRents[1][i] == lowest:
            removableGames.append(gamesAndRents[0][i])

    print("Games that aren't frequently rented:")
    for each in removableGames:
        print(each)

def feedback_evaulation(n):
    '''
    Takes in parameter n as the max value acting as a filter
    Gathers all games that received below that rating from the "Game_Feedback.txt" file
    Shows on a graph how many times each game received a rating below this inputted rating
    Displays each of these games in a text format, alongside comments that were also in the file
    '''
    rGame = [[],[],[]]

    feedbackList = db.database_access("Game_Feedback.txt")

    for each in feedbackList[1:]:
        # Check if the rating is below the specified threshold 'n'
        if int(each[1]) < n:
            # If yes, increment the no. of times the game received a low rating
            if each[0] in rGame[0]:
                rGame[1][rGame[0].index(each[0])] += 1
                if each[2] != "":
                    # Append comments to existing comments for the same game
                    if rGame[2][rGame[0].index(each[0])]:
                        rGame[2][rGame[0].index(each[0])] += ", "+each[2]
                    else:
                        rGame[2][rGame[0].index(each[0])] += each[2]
            else:
                # Adds gameID, sets count and adds comments to list
                rGame[0].append(each[0])
                rGame[1].append(1)
                rGame[2].append(each[2])

    # Check if there are games with ratings below 'n'
    if len(rGame[0]) != 0:
        print("\nThe following games were given ratings below "+str(n)+":")
        for each in range(len(rGame[0])):
            print(rGame[0][each] + " " + str(rGame[1][each]) + " times")
            if rGame[2][each] != "":
                print("Comments: "+rGame[2][each])
            else:
                print("No comments given")

    return rGame