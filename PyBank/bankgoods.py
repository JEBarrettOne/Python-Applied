import os 
import csv 
from statistics import mean


csvpath = "/Users/joshbarrett/Desktop/NU-VIRT-DATA-PT-11-2021-U-C/Python-Applied/PyBank/budget_data.csv"

#Establish lists for the profits/losses for each date, the months recorded, and counters for the highest & lowest values observed
nums = []
months = []
highchange = 0
lowchange = 0
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    csv_header = next(csvreader)
    #For each row read by the program, take the 1st index of the row and append it to the profit/loss list, and append the date
    #to the months list
    for row in csvreader:
        nums.append(row[1])
        months.append(row[0])
        #Convert the strings in this list to integers
        truenums = [int(i) for i in nums]
        #Now iterate through the integers list, starting with the 1st index and subtract the previous index to obtain the net
        #change between the periods, then append that value to a new list –– we can find the max and min to get our greatest
        #increase and decrease
        for i in truenums:
            delts = []
            for i in range(1, len(truenums)):
                delts.append(truenums[i] - truenums[i-1])
                highchange = max(delts)
                lowchange = min(delts)
                  
    #Perform final modification of the lists to get our metrics of interest    
    highrow = [months[delts.index(highchange)], highchange]
    lowrow = [months[delts.index(lowchange)], lowchange]
    duration = len(months)
    avgdelt = mean(delts)
    total = sum(truenums)

report = (
    f"{' Financial Analysis ':-^48}\n"
    f"{'Total Months:':24}{duration:24,.0f}\n"
    f"{'Net Profits:':24}{total:24,.0f}\n"
    f"{'Avg Change:':24}{avgdelt:24,.0f}\n"
    f"{'Max Increase:':14}{highrow[0]:^20}{highrow[1]:14,.0f}\n"
    f"{'Max Decrease:':14}{lowrow[0]:^20}{lowrow[1]:14,.0f}\n"
    f"{'--':-^48}"
)

print(report)

resource_path = "PyBank/financial_analysis.txt"
output_path = os.path.join("Output","financial_analysis.text")

with open(output_path, "w") as textfile:
    textfile.write(report)






        