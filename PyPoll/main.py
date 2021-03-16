# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 12:11:39 2021

@author: ramza
"""
import os
import zipfile
import csv

zf = zipfile.ZipFile("Raw_Data/election_data.zip")
csvpath = os.path.join(zf)

with open(csvpath, newline="") as csvfile:
    csv_reader =csv.reader(csvfile, delimiter=",")
    csv_headers = next(csv_reader, None)
    #print (f"CSV Header: {csv_headers}"

    # print heading 
    print ("Election Results")
    print ("-----------------------")


    # Variables
    candidate_list = []
    count_votes = 0
    
    # Loop through csv_reader
    for row in csv_reader:
        # if value in Candidate column is not in candidate_list,
        # append to candidate_list
        if row[2] not in candidate_list:
            count_votes += 1
            candidate_list.append(row[2])
        else: # if not in list, just add the vote count
            count_votes += 1

        # print (len(candidate_list)) = 4
    
    # count votes per candidate
    i = 0 
    num_candidates = len(candidate_list)
    candidate_votes = [0]*num_candidates

    for i in range(num_candidates):
        if row[2] == candidate_list[i]:
            candidate_votes[i] += 1

    most_vote = max(candidate_votes)
    vote_index = candidate_votes.index(most_vote)
    winner = candidate_list[vote_index]

    #print (winner)

    # percent per candidate
    j = 0
    percent_of_votes = []

    for j in range(num_candidates):
        percent = round(candidate_votes[j]/count_votes * 100,2)
        percent_of_votes.append(percent)


    print ("Election Results")
    print ("-----------------------------")
    print (f"Total Votes: {count_votes}")
    print ("-----------------------------")
    print (f"Name: {candidate_list} {percent_of_votes}, {candidate_votes}")
    print ("-----------------------------")
    print (f"Winner: {winner}")

exportpath = ("Results.txt")
with open(exportpath, "w") as textfile:
        textfile.write("Election Results")
        textfile.write("-----------------------------")
        textfile.write(f"Total Votes: {count_votes}")
        textfile.write("-----------------------------")
        textfile.write(f"Name: {candidate_list} {percent_of_votes}, {candidate_votes}")
        textfile.write("-----------------------------")
        textfile.write(f"Winner: {winner}")
    
