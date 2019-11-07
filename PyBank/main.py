import csv
import os

# Open the csv file
csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath, newline='') as csvfile:
    budget_data = csv.reader(csvfile, delimiter=',')

    # Skipping the first line
    csv_header = next(budget_data)

    # Variables

    total_months = 0
    net_loss_profit = 0
    greatest_increase = 0
    greatest_decrease = 0
    change_loss_profit = []
    first_value = 0.0

    for row in budget_data:

        # The total number of months included in the dataset
        total_months = total_months + 1

        # The net total amount of 'Profit/Losses' over the entire period
        net_loss_profit = net_loss_profit + int(row[1])
        value = int(row[1])

        # The greatest increase in profits (date and amount) over the entire period
        if value > greatest_increase:
            greatest_increase = int(row[1])
            month_increase = row[0]

        # The greatest decrease in losses (date and amount) over the entire period
        elif value < greatest_decrease:
            greatest_decrease = int(row[1])
            month_decrease = row[0]

        # The average of the changes in "Profit/Losses" over the entire period
        if first_value == 0.0:
            first_value = int(row[1])
        else:
            second_value = int(row[1])
            change_loss_profit.append(second_value - first_value)
            first_value = int(row[1])

average_loss_profit = float("{0:.2f}".format(sum(change_loss_profit) / (total_months - 1)))

# Print the analysis
print(f"-------------------------------------\n"
      f"        Financial Analysis\n"
      f"-------------------------------------\n"
      f"Total Months: {total_months}\n"
      f"Total Net Profit/Loss: $ {net_loss_profit}\n"
      f"Average Change: $ {average_loss_profit}\n"
      f"Greatest Increase in Profits: {month_increase} ($ {greatest_increase})\n"
      f"Greatest Decrease in Profits: {month_decrease} ($ {greatest_decrease})")

# Export a text (.txt) file with the results

output_path = os.path.join("budget_analysis.txt")
with open(output_path, 'w') as txtfile:
    txtfile.write(f"-------------------------------------\n"
                  f"        Financial Analysis\n"
                  f"-------------------------------------\n"
                  f"Total Months: {total_months}\n"
                  f"Total Net Profit/Loss: $ {net_loss_profit}\n"
                  f"Average Change: $ {average_loss_profit}\n"
                  f"Greatest Increase in Profits: {month_increase} ($ {greatest_increase})\n"
                  f"Greatest Decrease in Profits: {month_decrease} ($ {greatest_decrease})")

# Export a text (.csv) file with the results

output_path = os.path.join("budget_analysis.csv")
with open(output_path, 'w', newline='') as csvfile:
     budget_analysis = csv.writer(csvfile, delimiter=',')

     budget_analysis.writerow(
         ['Total_Months', 'Total_Net', 'Average_Change', 'Month_Great_Increase',
          'Value_Great_Increase', 'Month_Great_Decrease',
          'Value_Great_Decrease'])
     budget_analysis.writerow(
         [total_months, net_loss_profit, average_loss_profit, month_increase, greatest_increase, month_decrease,
          greatest_decrease])