# Import the necessary libraries for reading csv files
from pathlib import Path
import csv

# Set the path for the csv file
filepath = Path("../Resources/pokemon.csv")

# Create new lists to store data for heaviest and tallest pokemon
heaviest = []
tallest = []

# Open the csv
with open(filepath, 'r') as file:

    # Iterate through the data and search for the number the user inputted. Remember to skip the header of the CSV.
    file_reader = csv.reader(file, delimiter=',')
    next(file_reader)

    for entry in file_reader:
        # Print the name of the pokemon(identifier) and pokedex number(species id) at that number. For example, "Pokemon No. 25 - pikachu".
        print(f"Pokemon No. {entry[2]} - {entry[1]}")

        # Iterate through the data and search for pokemon whose weight is greater than 3000. Append only the pokemon's name and weight to the 'heaviest' list.
        if int(entry[4]) > 3000:
            heaviest.append(entry[1]+" - "+entry[4])

        # Iterate through the data and search for pokemon whose height is greater than 50. Append only the pokemon's name and height to the 'tallest' list.
        if int(entry[3]) > 50:
            tallest.append(entry[1]+" - "+entry[3])

# Print the list of heaviest and tallest pokemon
print(heaviest)
print(tallest)
