# Modules
import os
import csv
import pandas as pd


# Set path for file
csvpath = os.path.join("resources","budget_data.csv")


total = 0
months = 0
average = 0
#difference = 0
diff_list = []
previous = 0
current = 0
changes = []
highest = ["date",0,0]
lowest = ["date",0,0]
output = ''

# Open the CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    headers = next(csvreader, None)
    for row in csvreader:
        total = int(total) + int(row[1])
        months = months + 1
        #using the variable 'current' to make calculations to the current row
        current = row
        #calculating the change in profit/loss, appending that to the current row, then adding all of that to 'changes'
        diff = int(current[1]) - previous
        diff_list.append(int(current[1]) - previous)
        #net_diff = net_diff + diff
        current.append(diff)
        changes.append(current)
        previous = int(current[1])
        #Logic to determine which row of data has the highest and lowest changes in profits
        if int(current[2]) > int(highest[2]):
            highest = current
        elif int(current[2]) < int(lowest[2]):
            lowest = current
    del changes[0]
    del diff_list[0]
    #Calculating the average change
    average = sum(diff_list) / len(diff_list)

output = open('Analysis/output.txt','w')
output.write(f"""
Financial Analysis
----------------------------
Total Months: {months}
Total: {total} 
Average Change: ${average} 
Greatest Increase in Profits: {highest[0]} (${highest[2]}) 
Greatest Decrease in Profits: {lowest[0]} (${lowest[2]})
""")

print(f"""
Financial Analysis
----------------------------
Total Months: {months}
Total: {total} 
Average Change: ${average} 
Greatest Increase in Profits: {highest[0]} (${highest[2]}) 
Greatest Decrease in Profits: {lowest[0]} (${lowest[2]})
""")