# import os and csv modules
import os
import csv


# path for getting the CSV file
csvpath = os.path.join("Resources","election_data.csv")

#function for counting rows.  Returns the length of the csvfile (minus the header).
def count_rows(filename):
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        row_count = len(list(reader))
    return row_count

#function for returning a list of unique candidates from the election_data.csv file who received votes.
def candidates(csv_file, column_name):
    unique_candidates = set()
    with open(csv_file,'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  #Skip the header row

        for row in csv_reader:
            unique_candidates.add(row[column_name])
       
    return list(unique_candidates)

#call count_rows function to calculate the total number of votes cast.
total_votes = count_rows(csvpath)

#create a list of candidates
candidate_list = candidates(csvpath,2)

#Print the results to the terminal.
print("Election Results")
print("-------------------------------")
print(f"Total Months: {total_votes}")
print("-------------------------------")
print(f"{candidate_list}")
