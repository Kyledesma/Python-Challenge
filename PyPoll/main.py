# Modules
import os
import csv


# Set path for file
csvpath = os.path.join("resources","election_data.csv")


votes = 0
candidates = {}

# Open the CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    headers = next(csvreader, None)
    for row in csvreader:
        votes += 1
        if row[2] not in candidates.keys():
            candidates[row[2]] = 1
        elif row[2] in candidates.keys():
           candidates[row[2]] += 1
    v = list(candidates.values())
    k = list(candidates.keys())       
    winner = k[v.index(max(v))]    

print(f"""
Election Results
-------------------------
Total Votes: {sum(candidates.values())}
-------------------------
""")
for key,val in candidates.items():
    percent = val / sum(candidates.values())
    percent = "{:.3%}".format(percent)
    print(f'{key}: {percent} ({val})')
print(f"""    
-------------------------
Winner: {winner}
-------------------------

""")


output = open('Analysis/output.txt','w')
output.write(f"""
Election Results
-------------------------
Total Votes: {sum(candidates.values())}
-------------------------
""")
for key,val in candidates.items():
    percent = val / sum(candidates.values())
    percent = "{:.3%}".format(percent)
    output.write(f'{key}: {percent} ({val})\n')
output.write(f"""    
-------------------------
Winner: {winner}
-------------------------

""")



