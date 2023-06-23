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

    # prompt the user for a movie title
    movie_entry = input("What movie would you like to watch? ")

    # check whether the movie is available, and if so, provide additional details
    
