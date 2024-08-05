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

def get_candidates(csv_file, unique_column_index):
    unique_values_sum = {}
    
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)  # Skip the header row
        
        for row in reader:
            unique_value = row[unique_column_index]
            #sum_value = int(row[sum_column_index])  # Assuming the sum column contains numeric values
            sum_value = 1
            if unique_value not in unique_values_sum:
                unique_values_sum[unique_value] = 0
                
            unique_values_sum[unique_value] += sum_value
    
    return unique_values_sum

#call count_rows function to calculate the total number of votes cast.
total_votes = count_rows(csvpath)

#create a list of candidates along with the total votes for each candidate.
result = get_candidates(csvpath, 2)

#find the winner by finding the max value of the results dictionary from the get_candidates function.
winner = max(result,key=result.get)

#Print the results to the terminal.
print("Election Results\n")
print("-------------------------------\n")
print(f"Total Months: {total_votes}\n")
print("-------------------------------\n")
for unique_value, sum_value in result.items():
    print(f"{unique_value}: {(sum_value/total_votes):.3%}  ({sum_value})\n")
print("-------------------------------\n")
print(f"Winner: {winner}\n\n")

# Create a file called "election_analysis.txt" in the analysis folder.  
filepath = os.path.join("analysis","election_analysis.txt")

# Write to the to the "election_analysis.txt" file path
with open(filepath, "w") as file:
    file.write("Election Results\n\n")
    file.write("-------------------------------\n\n")
    file.write(f"Total Months: {total_votes}\n\n")
    file.write("-------------------------------\n\n")
    for unique_value, sum_value in result.items():
        file.write(f"{unique_value}: {(sum_value/total_votes):.3%} ({sum_value})\n\n")
    file.write("-------------------------------\n\n")
    file.write(f"Winner: {winner}\n")
    