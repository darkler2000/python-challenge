#PyBank

import os
import csv

csvpath = os.path.join("budget_data.csv")

total_months = 0
net_total = 0
#last_profit = 0
total_change = 0
gr_inc = [" ", 0]
gr_dec = [" ", 0]

#Read in the CSV file
with open(csvpath, 'r') as csvfile:

    #Split the data by comma
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    #Caluculate months
    

    for row in csvreader:



        #Caluclate net total
        net_total = net_total + int(row[1])

        #Calculate profit change
        try:
            change = int(row[1]) - last_profit
        except NameError:
            last_profit = int(row[1])
            continue
        last_profit = int(row[1])
        total_change = total_change + change

        #Calculate greatest increase in profits
        if change > int(gr_inc[1]):
            gr_inc = [row[0], change]

        #Calculate greatest decrease in profits
        if change < int(gr_dec[1]):
            gr_dec = [row[0], change]

        #Caluculate months
        total_months = total_months + 1

    profit_loss_avg = round(total_change/total_months, 2)



print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total : ${net_total}")
print(f"Average Change: ${profit_loss_avg}")
print(f"Greatest Increase in Profits: {gr_inc[0]} (${gr_inc[1]})")
print(f"Greatest Decrease in Profits: {gr_dec[0]} (${gr_dec[1]})")

with open('output.txt', 'w') as file:
    file.write("Financial Analysis\n")
    file.write("-----------------------------\n")
    file.write(f"Total Months: {total_months}\n")
    file.write(f"Total: ${net_total}\n")
    file.write(f"Average Change: ${profit_loss_avg}\n")
    file.write(f"Greatest Increase in Profits: {gr_inc[0]} (${gr_inc[1]})\n")
    file.write(f"Greatest Decrease in Profits: {gr_dec[0]} (${gr_dec[1]})\n")





