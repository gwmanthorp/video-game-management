# F322418
# 26/11/2023
'''
Simple database functionalities that are used elsewhere in the program are coded here
Allows other modules to access records, append to files or rewrite files
'''
def database_access(file_name):
    """
    Reads a database file and returns its contents as a list.
    Takes in the file name as a paramter and returns the converted list

    :param file_name: a string containing the name of the file to be accessed
    """

    file = open(file_name, "r")
    database = []
    # Read each line, strip whitespaces, and split into a list
    for each in file.readlines():
        each = each.strip()
        database.append(each.split(","))
    file.close()
    return database

def add_record(file_name, record):
    """
    Adds a record to a database file.
    Uses parameterised file name and record

    :param file_name: a string containing the name of the file to be added to
    :param record: a record that is to be added to the record
    """

    file = open(file_name, "a")
    record[-1] += "\n" # Last element set to have newline
    # Converts to a comma-separated string and append to the end of the file
    record = ",".join(record)
    file.write(record)

    file.close()

def return_game(file_name, database):
    """
    Writes the modified database back to the file after a game is returned.
    Uses parameterised file name and database

    :param file_name: a string containing the name of the file to be written to
    :param database: a list of all elements to be written to a file
    """

    file = open(file_name, "w")
    for record in database:
        record[-1] += "\n" # Last element set to have newline
        # Converts to a comma-separated string and append to the end of the file
        record = ",".join(record)
        file.write(record)

    file.close()