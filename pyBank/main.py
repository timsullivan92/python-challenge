# import os and csv modules
import os
import csv

csvpath = os.path.join("Resources","budget_data.csv")


#function for counting rows
def count_rows(filename):
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        row_count = len(list(reader))
    return row_count

#function for calculating total profit
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


#call count_rows function
total_months = count_rows(csvpath)

#call profit_total function
total = profit_total(csvpath)

#call get value
start_pl = get_value(csvpath, 1,1)
end_pl = get_value(csvpath,total_months,1)
#change_pl = 0
change_pl = float(end_pl) - float(start_pl)
average_pl = change_pl / (total_months -1)  

   
print(f"Total Months: {total_months}")
print(f"Total: {total}")
print(f"PL start: {start_pl}")
print(f"PL end: {end_pl}")
print(f"PL Change: {change_pl}")
print(f"Average Change: {average_pl}")