# import the necessary libraries
from pathlib import Path
import csv

# set the path to the csv file
filepath = Path("../Resources/netflix_ratings.csv")

# open the csv file and set up the reader iterator
with open(filepath,"r") as file:
    file_reader = csv.reader(file, delimiter=",")

    # remember to omit the header row
    next(file_reader)

    # set a found flag
    selection_found = False

    # prompt the user for a movie title
    selection = input("What movie would you like to watch? ")

    # check whether the movie is available, and if so, provide additional details
    for entry in file_reader:
        if selection.lower() == entry[0].lower():
            print(f"{entry[0]} is rated {entry[1]} with a rating of {entry[5]}")
            selection_found = True
            break
    
    # return a message if the movie selection wasn't located in Netflix's library
    if not selection_found: print(f"Your movie selection {selection} is not currently available on Netflix")
