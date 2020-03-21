import os
import csv
import pandas as pd

# Path to collect data from the Resources folder
pybank_csv = os.path.join( "Resources", "election_data.csv")
candidate_votes = {}
with open(pybank_csv) as csvfile:
    reader = csv.reader(csvfile)
    csv_header = next(reader)
    for row in reader:
        candidate = row[2]
        if candidate in candidate_votes.keys():
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1
total_votes = sum(candidate_votes.values())
percent = []
print(f"Total Votes: {total_votes}")

for i in candidate_votes: 
    percent = round(float(candidate_votes[i] / total_votes) * 100, 2)
    print(f" {i}: {percent}% ({candidate_votes[i]})")
for key in candidate_votes.keys():
    if candidate_votes[key] == max(candidate_votes.values()):
        winner = key
print(f'Winner:  {winner}')
