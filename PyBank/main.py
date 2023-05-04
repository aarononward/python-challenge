import os
import csv

csvpath = os.path.join(".", "Resources","budget_data.csv")
    
month = []
ProfitLoss = []

with open(csvpath) as csvfile:

    csv_reader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csv_reader)
    for row in csv_reader:
        month.append(row[0])
        ProfitLoss.append(int(row[1]))

        month_count = len(month)
        total = sum(ProfitLoss)
        avg_change = total/month_count

    
print(month_count)
print(total)
print(avg_change)    





