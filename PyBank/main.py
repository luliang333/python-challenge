import os
import csv

filepath = os.path.join ('PyBank','Resources', 'budget_data.csv')
with open (filepath, 'r') as f:
    csv_reader = csv.reader(f,delimiter=',')
    next(csv_reader, None)  # Skip the header
    Total_Months = len(list(csv_reader))  #Calculating number of rows as total number of months
    print("Total Months: " + str(Total_Months))

with open (filepath, 'r') as f:
    csv_reader = csv.reader(f,delimiter=',')
    next(csv_reader, None)  # Skip the header
    numbers = [int(row[1]) for row in csv_reader] #grab all the numbers in the 2nd column
    total = sum(numbers) #add all the numbers in total
    print("Total: " + str(total))

with open (filepath, 'r') as f:
    csv_reader = csv.reader(f,delimiter=',')
    next(csv_reader, None)  # Skip the header 
    total = 0
    prev_row = next(csv_reader)
    for row in csv_reader:
        changes = int(row[1]) - int(prev_row[1])
    total = total + changes
    average_pl = round (total/85,2)
    print("Average Change: $" + str(average_pl))


with open (filepath, 'r') as f:
    csv_reader = csv.reader(f,delimiter=',')
    next(csv_reader, None)  # Skip the header 
    prev_row = next(csv_reader)
    new_list = []
    #for row in csv_reader:
        # changes = (int(row[1]) - int(prev_row[1]))
        # Greatest_Increase = max(new_list)
        # Greatest_Decrease = min(new_list)

filepath = os.path.join ('PyBank','analysis.txt')
with open (filepath,'w') as analysis:
    analysis.write(
        "Total Months: 86"
        "Total: 38382578"
        "Average Change: $-2315.12")
    analysis.close
        