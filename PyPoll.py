#PyPoll

import os
import csv

total_votes = 0
CCS_total = 0
DDG_total = 0
RAD_total = 0
CCS_per = 0
DDG_per = 0
RAD_per = 0
winner = " "


csvpath = os.path.join("election_data.csv")

with open(csvpath, 'r') as csvfile:
       
    #Split the data by comma
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    for row in csvreader:

        #Calculate CCS votes
        if row[2] == "Charles Casper Stockham":
            CCS_total = CCS_total + 1
        elif row[2] == "Diana DeGette":
            DDG_total = DDG_total +1
        else:
            RAD_total = RAD_total + 1
    

#Caluculate total votes
total_votes = CCS_total + DDG_total + RAD_total

#Calculate percetages
CCS_per = round(CCS_total/total_votes, 5)*100
DDG_per = round(DDG_total/total_votes, 5)*100
RAD_per = round((RAD_total/total_votes)*100, 3)

print(CCS_total, RAD_total, CCS_per, RAD_per, total_votes, CCS_total/total_votes, RAD_total/total_votes, round((RAD_total/total_votes)*100, 5))

#Find Winner
winning_total = max(CCS_total, DDG_total, RAD_total)
if winning_total == CCS_total:
    winner = "Charles Casper Stockham"
elif winning_total == DDG_total:
    winner = "Diana DeGette"
else:
    winner = "Raymon Anthony Doane"

print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
print(f"Charles Casper Stockham: {CCS_per}% ({CCS_total})")
print(f"Diana DeGette: {DDG_per}% ({DDG_total})")
print(f"Raymon Anthony Doane: {RAD_per}% ({RAD_total})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

with open('output.txt', 'w') as file:
    file.write("Election Results\n")
    file.write("-------------------------\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write("-------------------------\n")
    file.write(f"Charles Casper Stockham: {CCS_per}% ({CCS_total})\n")
    file.write(f"Diana DeGette: {DDG_per}% ({DDG_total})\n")
    file.write(f"Raymon Anthony Doane: {RAD_per}% ({RAD_total})\n")
    file.write("-------------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write("-------------------------\n")









