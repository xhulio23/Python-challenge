# Import modules
import os
import csv

# Locating budget data
budget_data = "C:\\Users\\xhuli\\OneDrive\\Desktop\\Starter_Code\\PyBank\\Resources\\budget_data.csv"

# Variables 
header_row = []
period_change = 0
count_period = 0
net_value = 0
profits_losses = []
dates = []
# Reading the budget data file
with open(budget_data, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    # Header row
    header_row = next(csv_reader)  
    header_row = next(csvfile).split(",")

    # Reading the first row of the budget data
    first_row = next(csv_reader)
    period_change += 1
    net_value = net_value + int(first_row[1])


    # Checking the index of the date column
    date_index = 0
    if header_row[0] == "Date":
        date_index = 0
    elif header_row[1] == "Date":
        date_index = 1

        # Passing through each row of the data set
        dates.append(row[date_index])

        # Calculate the change
        period_change = int(row[1]) - net_value
        profits_losses.append(change)
        net_value = int(row[1])

        # Number of months
        period_change += 1

        # Total Profit/Losses over the entire campaign
        count_period = count_period + int(row[1])

    # Largest profits
    greatest_increase = max(profits_losses)
    greatest_index = profits_losses.index(greatest_increase)
    greatest_date = dates[greatest_index]

    # Lowest profits
    greatest_decrease = min(profits_losses)
    worst_index = profits_losses.index(greatest_decrease)
    worst_date = dates[worst_index]

    # Average in "Profit/Losses between months over the entire campaign period"
    avg_change = sum(profits_losses) / len(profits_losses)

# Final Report
print("Financial Analysis")
print("---------------------")
print(f"Total Months: {str(period_change)}")
print(f"Total: ${str(net_value)}")
print(f"Average Change: ${str(round(avg_change, 2))}")
print(f"Greatest Increase in Profits: {greatest_date} (${str(greatest_increase)})")
print(f"Greatest Decrease in Profits: {worst_date} (${str(greatest_decrease)})")



