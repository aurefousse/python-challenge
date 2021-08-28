import os
import csv

filepath = os.path.join('/Users/aurelianfousse/Desktop/UCSD Bootcamp/Homework/Homework 3 - Python 1/python-challenge/PyPoll/Resources/election_data.csv')
with open(filepath, 'r') as f:
    csv_reader = csv.reader(f, delimiter=',')

    next (csv_reader)
    totalvotes = 0
    
    khanvotes = 0
    correyvotes = 0
    livotes = 0
    otooleyvotes =0
    
    for row in csv_reader:
        totalvotes += 1

        voteID = row[0]
        county = row[1]
        candidate = row[2]

        if candidate == "Khan":
            khanvotes += 1

        if candidate == "Correy":
            correyvotes += 1

        if candidate == "Li":
            livotes += 1

        if candidate == "O'Tooley":
            otooleyvotes += 1

            candidatelist = {"Khan": khanvotes, "Correy": correyvotes, "Li": livotes, "O'Tooley": otooleyvotes}
            max_key = max(candidatelist, key=candidatelist.get)

print("Election Results")
print("-------------------------")
print(f"Total Votes: {totalvotes}")
print("-------------------------")

perckhanvotes = round(100 * khanvotes/totalvotes)
print(f"Khan: {perckhanvotes}% ({khanvotes})")

perccorreyvotes = round(100 * correyvotes/totalvotes)
print(f"Correy: {perccorreyvotes}% ({correyvotes})")

perclivotes = round(100 * livotes/totalvotes)
print(f"Li: {perclivotes}% ({livotes})")

percotooleyvotes = round(100 * otooleyvotes/totalvotes)
print(f"O'Tooley: {percotooleyvotes}% ({otooleyvotes})")

print("-------------------------")
print(f"Winner: {max_key}\n")
print("-------------------------")

outputfilepath = '/Users/aurelianfousse/Desktop/UCSD Bootcamp/Homework/Homework 3 - Python 1/python-challenge/PyPoll/main_text.txt'
if os.path.isfile(outputfilepath):
    os.remove(outputfilepath)

with open(outputfilepath, 'a') as f:
    f.write("Election Results\n")
    f.write("-------------------------\n")
    f.write(f"Total Votes: {totalvotes}\n")
    f.write("-------------------------\n")

    perckhanvotes = round(100 * khanvotes/totalvotes)
    f.write(f"Khan: {perckhanvotes}% ({khanvotes})\n")

    perccorreyvotes = round(100 * correyvotes/totalvotes)
    f.write(f"Correy: {perccorreyvotes}% ({correyvotes})\n")

    perclivotes = round(100 * livotes/totalvotes)
    f.write(f"Li: {perclivotes}% ({livotes})\n")

    percotooleyvotes = round(100 * otooleyvotes/totalvotes)
    f.write(f"O'Tooley: {percotooleyvotes}% ({otooleyvotes})\n")

    f.write("-------------------------\n")
    f.write(f"Winner: {max_key}\n")
    f.write("-------------------------\n")

