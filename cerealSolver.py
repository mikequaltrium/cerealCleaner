#import modules
import os
import csv 

#open csv file
cerealCSV = os.path.join(".","cereal.csv")
with open(cerealCSV, "r") as csvfile:
    #create csv reader 
    csvreader = csv.reader(csvfile, delimiter=",")

    csvHeader = next(csvreader)
    print(f"The header is: {csvHeader}")

    #iterate rows
    for row in csvreader:
        #if cereal contains 5 orr more grams of fiber, print
        if( float(row[7])) >= 5:
            print(row)

