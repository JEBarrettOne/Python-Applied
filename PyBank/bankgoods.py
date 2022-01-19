import os 
import csv 
from statistics import mean
import math

csvpath = "/Users/joshbarrett/Desktop/NU-VIRT-DATA-PT-11-2021-U-C/Python-Applied/PyBank/budget_data.csv"
nums = []
months = []
highchange = 0
lowchange = 0
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    csv_header = next(csvreader)
    
    for row in csvreader:
        nums.append(row[1])
        months.append(row[0])
        truenums = [int(i) for i in nums]
        high = 0
        low = 0
        for i in truenums:
            delts = []
            for i in range(1, len(truenums)):
                delts.append(truenums[i] - truenums[i-1])
                highchange = max(delts)
                lowchange = min(delts)
                  
        
    highrow = [months[delts.index(highchange)], highchange]
    lowrow = [months[delts.index(lowchange)], lowchange]
    duration = len(months)
    avgdelt = "{:.2f}".format(mean(delts))
    total = sum(truenums)

print(highrow)
print(lowrow)
print(total)
print(avgdelt)
print(duration)






        