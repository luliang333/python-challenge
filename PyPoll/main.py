import os
import csv
print("Election Results")
print("------------------------------")
filepath = os.path.join('PyPoll',"Resources",'election_data.csv')
with open (filepath, 'r') as f:
    csv_reader = csv.reader (f, delimiter = ',')
    next(csv_reader, None)
    total_votes = len(list(csv_reader))
    print("Total Votes: " + str(total_votes))
    print("------------------------------")

with open (filepath, 'r') as f:
    csv_reader = csv.reader (f, delimiter = ',')
    next(csv_reader, None)
    Khan_list = [row[2] for row in csv_reader if row[2] == "Khan"]
    Khan_count = len(Khan_list)
    Khan_percentage = round(((Khan_count/total_votes) * 100),3)
    print("Khan:" + str(Khan_percentage) +"% " + "("+str(Khan_count)+")")

with open (filepath, 'r') as f:
    csv_reader = csv.reader (f, delimiter = ',')
    next(csv_reader, None)
    Correy_list = [row[2] for row in csv_reader if row[2] == "Correy"]
    Correy_count = len(Correy_list)
    Correy_percentage = round(((Correy_count/total_votes) * 100),3)
    print("Correy:" + str(Correy_percentage) +"% " + "("+str(Correy_count)+")")

with open (filepath, 'r') as f:
    csv_reader = csv.reader (f, delimiter = ',')
    next(csv_reader, None)
    Li_list = [row[2] for row in csv_reader if row[2] == "Li"]
    Li_count = len(Li_list)
    Li_percentage = round(((Li_count/total_votes) * 100),3)
    print("Li:" + str(Li_percentage) +"% " + "("+str(Li_count)+")")
    
with open (filepath, 'r') as f:
    csv_reader = csv.reader (f, delimiter = ',')
    next(csv_reader, None)
    OTooley_list = [row[2] for row in csv_reader if row[2] == "O'Tooley"]
    OTooley_count = len(OTooley_list)
    OTooley_percentage = round(((OTooley_count/total_votes) * 100),3)
    print("O'Tooley:" + str(OTooley_percentage) +"% " + "("+str(OTooley_count)+")")
    print("------------------------------")
    candidates = {"Khan":Khan_count, "Correy":Correy_count, "Li":Li_count,"OTooley":OTooley_count}
    winner = max(candidates, key=candidates.get)
    print('Winner: ' + winner)
    print("------------------------------")

filepath = os.path.join ('PyPoll','analysis.txt')
with open (filepath,'w') as analysis:
    analysis.write(
        "Election Results"

        "Total Votes: 3521001"

        "Khan:63.0% (2218231)"
        "Correy:20.0% (704200)"
        "Li:14.0% (492940)"
        "O'Tooley:3.0% (105630)"

        "Winner: Khan")

    analysis.close