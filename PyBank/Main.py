#Import libraries
import os
import csv

csvfile = os.path.join('Resources', 'budget_data.csv')

    csvreader = csv.reader(csvfile)
    header = next(csvreader)  # Skip header row

 # Variables
    total_months = 0
    total_profit = 0
    prev_profit = 0
    max_profit_month = ""
    min_profit_month = ""
    max_profit = float('-inf')
    min_profit = float('inf')
    total_profit_change = 0

  # Reading each row in the CSV file
    for row in csvreader:
        total_months += 1
        total_profit += int(row[1])

  # Calculating the change in profit from the previous month
        profit_change = int(row[1]) - prev_profit
        prev_profit = int(row[1])

  # Updating max and min profit and corresponding month
        if profit_change > max_profit:
            max_profit = profit_change
            max_profit_month = row[0]

        elif profit_change < min_profit:
            min_profit = profit_change
            min_profit_month = row[0]
        
  # Calculating the total profit change
        total_profit_change += profit_change
            
  # Calculating the average profit change
        if total_months > 1:
            avg_profit_change = total_profit_change / (total_months -1)
            avg_profit_change = round(avg_profit_change, 2)
        else:
            avg_profit_change = 0

  # Calculating the total net profit
        net_profit = total_profit
        net_profit = round(net_profit, 2)

    
    # Print results
    print(f"Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: ${total_profit}")
    print(f"Average Change: ${avg_profit_change}")
    print(f"Greatest Increase in Profits: {max_profit_month} (${max_profit})")
    print(f"Greatest Decrease in Profits: {min_profit_month} (${min_profit})")

with open('Analysis/financial_analysis.txt', 'w') as output_file:
    output_file.write("Financial Analysis\n")
    output_file.write("----------------------------\n")
    output_file.write(f"Total Months: {total_months}\n")
    output_file.write(f"Total: ${total_profit}\n")
    output_file.write(f"Average Change: ${avg_profit_change:.2f}\n")
    output_file.write(f"Greatest Increase in Profits: {max_profit_month} ${max_profit}\n")
    output_file.write(f"Greatest Decrease in Profits: {min_profit_month} ${min_profit}\n") 
