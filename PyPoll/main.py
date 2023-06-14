import os
import csv

csvpath = os.path.join(".","Resources","election_data.csv")

charles = []
diana = []
raymon = []

with open(csvpath) as csvfile:
        csv_reader = csv.reader(csvfile, delimiter= "," )
        csvheader = next(csv_reader)
        for row in csv_reader:
            if row[2] == 'Raymon Anthony Doane':
                 raymon.append(row[0])
            raymon_count = len(raymon)

            if row[2] == 'Charles Casper Stockham':
                charles.append(row[0])
            charles_count = len(charles)

            if row[2] == 'Diana DeGette':
                diana.append(row[0])
            diana_count = len(diana)    

            total = raymon_count + charles_count + diana_count

            charles_per = charles_count / total * 100
            charles_per = "{:.3f}".format(round(float(charles_per), 3))
            
            diana_per = diana_count / total * 100
            diana_per = "{:.3f}".format(round(float(diana_per), 3))
            
            raymon_per = raymon_count / total *100
            raymon_per = "{:.3f}".format(round(float(charles_per), 3))

            names_n_votes = {"Charles Casper Stockham" : charles_count, "Diana DeGette" : diana_count, "Raymon Anthony Doane" : raymon_count}
            winner = max(names_n_votes, key = names_n_votes.get)


print('Election Results')
print("")
print('--------------------')
print("")
print('Total Votes: ' + str(total))            
print("")
print('--------------------')
print("")
print('Charles Casper Stockham: ' + str(charles_per) + '%' +
       ' (' + str(charles_count) + ')')
print("")
print('Diana Degette: ' +  str(diana_per) + '%' + ' (' + str(diana_count) + ')')   
print("")
print('Raymon Anthony Doane: ' + str(raymon_per) + '%' + ' (' + str(raymon_count) + ')')  
print("")
print('--------------------')
print("")
print('Winner: ' + str(winner))
print("")
print('--------------------')

with open(os.path.join(".","Analysis","Pypoll_Analysis.txt"), "w") as txtfile:
    
    txtfile.write('Election Results\n')
    txtfile.write("\n")
    txtfile.write('--------------------\n')
    txtfile.write('\n')
    txtfile.write('Total Votes: ' + str(total) + '\n')            
    txtfile.write("\n")
    txtfile.write('--------------------\n')
    txtfile.write("\n")
    txtfile.write('Charles Casper Stockham: ' + str(charles_per) + '%' +
       ' (' + str(charles_count) + ')\n')
    txtfile.write("\n")
    txtfile.write('Diana Degette: ' +  str(diana_per) + '%' + ' (' + str(diana_count) + ')' + '\n')   
    txtfile.write("\n")
    txtfile.write('Raymon Anthony Doane: ' + str(raymon_per) + '%' + ' (' + str(raymon_count) + ')\n')  
    txtfile.write("\n")
    txtfile.write('--------------------\n')
    txtfile.write("\n")
    txtfile.write('Winner: ' + str(winner) + '\n')
    txtfile.write("\n")
    txtfile.write('--------------------')