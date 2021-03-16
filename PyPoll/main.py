# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 12:11:39 2021

@author: ramza
"""
import os
import csv

# Set the path for the CSV file in PyPollcsv

PyPoll = os.path.join("PyPoll/Raw_Data/election_data.csv")

# Create the lists to store data and initialize

count = 0
candidatelist = []
unique_candidate = []
vote_count = []
vote_percent = []

# Open the CSV using the set path PyPoll

with open(PyPoll, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    
    # Loop through csvreader
    for row in csvreader:
        # Count the total number of votes
        count = count + 1
        # Set the candidate names to candidatelist
        candidatelist.append(row[2])
        # Create a set from the candidatelist to get the unique candidate names
    for x in set(candidatelist):
        unique_candidate.append(x)
        # counting total number of votes per candidate (y)
        y = candidatelist.count(x)
        vote_count.append(y)
        # z is the percent of total votes per candidate
        z = round((y/count)*100,2)
        vote_percent.append(z)
        
    winning_vote_count = max(vote_count)
    winner = unique_candidate[vote_count.index(winning_vote_count)]

#Printing Results in the terminal  

print("-------------------------")
print("Election Results")   
print("-------------------------")
print("Total Votes :" + str(count))    
print("--------------------------------------------")
print("Votes per candidate-------------------------")
for i in range(len(unique_candidate)):
            print(unique_candidate[i] + ": " + str(vote_percent[i]) +"% (" + str(vote_count[i])+ ")")
print("-------------------------")
print('Maximum votes obtained by a single candidate were '+(str(winning_vote_count)))
print("The winner is: " + winner)
print("-------------------------")

# Print to a text file: election_results.txt

with open('pyPoll/election_results.txt', 'w') as text:
    text.write("Election Results\n")
    text.write("---------------------------------------\n")
    text.write("Total Votes: " + str(count) + "\n")
    text.write("----------------------------------------------------------\n")
    text.write("Votes per candidate---------------------------------------\n")
    for i in range(len(set(unique_candidate))):
        text.write(unique_candidate[i] + ": " + str(vote_percent[i]) +"% (" + str(vote_count[i]) + ")\n")
    text.write("---------------------------------------\n")
    text.write("The winner is: " + winner + "\n")
    text.write("---------------------------------------\n")