# import os and csv modules
import os
import csv

# path for getting the CSV file
csvpath = os.path.join("Resources","budget_data.csv")

#function for counting rows.  Returns the length of the csvfile (minus the header)
def count_rows(filename):
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        row_count = len(list(reader))
    return row_count

#function for calculating total profit.  Sums the profit/loss column for each row in the CSV file.
def profit_total(filename):
    total = 0
    with open(filename,'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            total += float(row[1])
    return total

#function for calculating the profit/loss value for a specific row,column
def get_value(filename, row_number, column_index):
    with open(filename,'r') as csvfile:
        reader = csv.reader(csvfile)
        for i, row in enumerate(reader):
            if i == row_number:
                return row[column_index]
            
#function for calculating greatest difference.  Compares the profit/loss value for each row to the previous row 
# and returns the greatest increase.
def greatest_increase(filename):
    with open(filename,'r') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)  #skip the header row

        previous_value = None
        greatest_increase = 0

        for row in reader:
            value = float(row[1])   
            #calculate the increase from the previous value
            if previous_value is not None:
                increase = value - previous_value
                if increase > greatest_increase:
                    greatest_increase = increase
                    date = row[0]

            previous_value = value
            
    return date, greatest_increase

#function for calculating greatest decrease.  Compares the profit/loss value for each row to the previous row 
# and returns the greatest decrease.
def greatest_decrease(filename):
    with open(filename,'r') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)  #skip the header row

        previous_value = None
        greatest_decrease = 0

        for row in reader:
            value = float(row[1])   
            #calculate the increase from the previous value
            if previous_value is not None:
                increase = value - previous_value
                if increase < greatest_decrease:
                    greatest_decrease = increase
                    date = row[0]

            previous_value = value
            
    return date, greatest_decrease


#call count_rows function to calculate the total number of months.
total_months = count_rows(csvpath)

#call profit_total function to calculate the Total profit/loss for all months.
total = profit_total(csvpath)

#call get value function to get the profit/loss for the first row after header (start_pl) 
# and the last profit/loss value in the column (end_pl).
start_pl = get_value(csvpath, 1,1)
end_pl = get_value(csvpath,total_months,1)

#Calculate the total change (from first month to last month) and the average
change_pl = float(end_pl) - float(start_pl)
average_pl = change_pl / (total_months -1) 

#get greatest increase between two rows for the profit/loss column
result = greatest_increase(csvpath)
gi_date, gi_diff = result

#get greatest decrease between two rows for the profit/loss column
result = greatest_decrease(csvpath)
gd_date, gd_diff = result


#Print the results to the terminal.
print(f"Total Months: {total_months}")
print(f"Total: ${round(total)}")
print(f"Average Change: ${round(average_pl,2)}")
print(f"Greatest Increase in Profits:  {gi_date} (${round(gi_diff)})")
print(f"Greatest Decrease in Profits:  {gd_date} (${round(gd_diff)})")


# Create a file called "financial_analysis.txt" in the analysis folder.  
filepath = os.path.join("analysis","financial_analysis.txt")

# Write to the to the "financial_analysis.txt" file path
with open(filepath, "w") as file:
    file.write("Analysis Results:\n")
    file.write("-----------------\n")
    file.write(f"Total Months: {total_months}\n")
    file.write(f"Total: ${round(total)}\n")
    file.write(f"Average Change: ${round(average_pl,2)}\n")
    file.write(f"Greatest Increase in Profits: {gi_date} (${round(gi_diff)})\n")
    file.write(f"Greatest Decrease in Profits: {gd_date} (${round(gd_diff)})\n")