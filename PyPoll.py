# Data we need to retrieve:
    # 1: Total numbers of votes cast
    # 2: A list of candidates who received votes
    # 3: Percent of votes each won
    # 4: Total number of votes each won
    # 5: Winner based on popular vote 

import csv
import os
file_to_load = "./Resources/election_results.csv"
#print(file_to_load)

#with open(file_to_load) as election_data
    #print(election_data)

# Create a filename variable
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Use open() to write to file 
#open(file_to_save, "w")

# Create and initialize a total vote counter variable at 0
total_votes = 0

#Declare a new list
candidate_options = []
#Declare an empty dictionary
candidate_votes = {}

# Create variables for Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    #Print the header rows
    #print(headers)

    # Print each row in file
    for row in file_reader:
        #print(row)
        total_votes += 1

        # Print the candidate name from each row.
        candidate_name = row[2]
        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)
            #print(candidate_options)
            # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

    # Determine the percentage of votes for each candidate by looping through the counts.
    # 1. Iterate through the candidate list.
    for candidate_name in candidate_votes:
        # 2. Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
        # 3. Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100

        # 4. Print the candidate name and percentage of votes.
        #print(f"{candidate_name}: received {vote_percentage}% of the vote.")

        # print out each candidate's name, vote count, and percentage of votes
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)

        # Determine winning vote count and candidate
        # 1. Determine if the votes is greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # 2. If true then set winning_count = votes and winning_percent = vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
            # 3. And, set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name

        # Print out the winning candidate, vote count and percentage to terminal.
    winning_candidate_summary = (
            f"------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"-------------------------\n")
    print(winning_candidate_summary)
        
            




