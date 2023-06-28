# @TODO: Your code here

# import the required libraries for Path and csv
from pathlib import Path
import csv

# set the file path reference
filepath = Path("../Resources/employees.csv")

# open the file and read in the data
with open(filepath, "r") as file:
    # set the file iterator
    file_reader = csv.reader(file, delimiter=",")
    # omit the header
    next(file_reader)
    # create an empty data struture to populate with employee data
    new_employee_data = []
    # load the data content into a dictionary structure
    for employee in file_reader:
        # populate the data entry element from the file entry
        data_entry = {}
        data_entry["first_name"] = employee[0]
        data_entry["last_name"] = employee[1]
        data_entry["ssn"] = employee[2]
        data_entry["email"] = employee[0]+"."+employee[1]+"@deathstart.org"
        # add the employee data into the new database
        new_employee_data.append(data_entry)

# set the output file path
output_path = Path('UpdatedEmployeeData.csv')
# write out the new employee database to file
with open(output_path, 'w') as output_file:
    # set the writer iterator object
    fieldnames = ['first_name', 'last_name', 'ssn', 'email']
    file_writer = csv.DictWriter(output_file,fieldnames=fieldnames)
    # write out the header
    file_writer.writeheader()
    # loop through the employee database and write it out to the output file - without a header
    for data_item in new_employee_data:
        file_writer.writerow(data_item)
