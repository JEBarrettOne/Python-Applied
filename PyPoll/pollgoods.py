import os 
import csv 


csvpath = "/Users/joshbarrett/Desktop/NU-VIRT-DATA-PT-11-2021-U-C/Python-Applied/PyPoll/election_data.csv"
vote_dict = {}

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    csv_header = next(csvreader)

    for row in csvreader:
        # Look for the candidate name as the 2nd index of each row within the dictionary, then if found in the dictionary
        # increase the count of the value by 1
        if(row[2] in vote_dict ):
           vote_dict[row[2]]+=1
        # If the candidate is not found as a key in the dictionary, create that key within the dictionary
        else:
            vote_dict[row[2]] = 1
    # An alternative solution: vote_dict[row[2]] = vote_dict.get(row[2],0) + 1 to create a list from the dictionary entries
    # that uses the 2nd index of the row (candidate) to create a new key in the dictionary, set its value to 0, and then add 
    # 1 to that value for the vote

#Add all values for each key (candidate) in the dictionary
totalvotes= sum(vote_dict.values())
#Identify winner as the key associated with the largest value using .get on the dictionary
winner = max(vote_dict, key=vote_dict.get)
#Create a new list that displays the key (candidate), followed by the value (votes received) and the proportion of
#the associated value to the total value of the entries in the dictionary
lines = [
    f"{k + ':':12}" f"{vote_dict[k]:12,}" f"{vote_dict[k]/totalvotes * 100:12,.2f}%\n"
    for k in vote_dict
]

report = (
    f"{' Election Results ':^36}\n"
    f"{'--':-^36}\n"
    f"{'Total Votes:':12}{totalvotes:12,}{100:11,.2f}%\n"
    f"{'--':-^36}\n"
    f"{''.join(lines)}"
    f"{'--':-^36}\n"
    f"{'Winner:':12}{winner:>12}\n"
    f"{'--':-^36}\n"
)

print(report)

resource_path = "PyPoll/election_analysis.txt"
output_path = os.path.join("Output","election_analysis.text")

with open(output_path, "w") as textfile:
    textfile.write(report)