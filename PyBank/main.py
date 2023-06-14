import os
import csv

csvpath = os.path.join(".","Resources","budget_data.csv")
    
month = []
ProfitLoss = []
monthly_diff  = []

with open(csvpath) as csvfile:

    csv_reader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csv_reader)
    for row in csv_reader:
        month.append(row[0])
        ProfitLoss.append(int(row[1]))

        month_count = len(month)
        total = sum(ProfitLoss)
        
for i, val in enumerate(ProfitLoss):
    if (i == (len(ProfitLoss)-1)):
        break
    else:
        monthly_diff.append(ProfitLoss[i+1] - ProfitLoss[i])

month_trim = month[1:]

avg_change= sum(monthly_diff)/len(monthly_diff)
avg_change = "${:,.2f}".format(avg_change)

zip_dif = list(zip(month_trim,monthly_diff))


max_dif = max(zip_dif, key = lambda x:x[1])


min_dif = min(zip_dif, key = lambda x:x[1]) 

print("Financial Analysis")
print("")
print("-----------------------")
print("")
print("Total Months: " + str(month_count))
print("Total: " + "$"+ str(total))
print("Average Change: " + str(avg_change))    
print("Greatest Increase in Profits: " + \
       str(max_dif[0]) + " " + "$"+ str(max_dif[1]))
print("Greatest Decrease in Profits: " + \
        str(min_dif[0]) + " " + "$"+ str(min_dif[1]))


with open(os.path.join(".","Analysis","PyBank_Analysis.txt"), "w") as txtfile:

    txtfile.write("Financial Analysis\n")
    txtfile.write("\n")
    txtfile.write("-----------------------\n")
    txtfile.write("\n")
    txtfile.write("Total Months: " + str(month_count) + "\n")
    txtfile.write("\n")
    txtfile.write("Total: " + "$"+ str(total) + "\n")
    txtfile.write("\n")
    txtfile.write("Average Change: " + str(avg_change) + "\n")  
    txtfile.write("\n")
    txtfile.write("Greatest Increase in Profits: " + \
            str(max_dif[0]) + " " + "$"+ str(max_dif[1]) + "\n")
    txtfile.write("\n")
    txtfile.write("Greatest Decrease in Profits: " + \
            str(min_dif[0]) + " " + "$"+ str(min_dif[1]) + "\n")

txtfile.close()


