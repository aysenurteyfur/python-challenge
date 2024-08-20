#import libraries
import os
import csv

elecfile = os.path.join('Resources', 'election_data.csv')

with open(elecfile) as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)  # Skip header row

    # Variables
    total_votes = 0
    candidate_votes = {}
    winner = ""
    max_votes = 0

    # Reading through each row in the CSV file
    for row in csvreader:
        total_votes += 1
        candidate = row[2]

        # Updating the candidate's vote count
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1

        # Updating the winner
        if candidate_votes[candidate] > max_votes:
            max_votes = candidate_votes[candidate]
            winner = candidate

    # Calculating the percentage of votes each candidate received
    vote_percentages = {candidate: (votes / total_votes) * 100 for candidate, votes in candidate_votes.items()}

    # Printing results
    print(f"Election Results")
    print("-------------------------")
    print(f"Total Votes: {total_votes}")
    print("-------------------------")
    for candidate, votes in candidate_votes.items():
        percentage = round(vote_percentages[candidate], 3)
        print(f"{candidate}: {percentage}% ({votes})")
        print(f"-------------------------")
    print(f"Winner: {winner}")


with open('Analysis/election_results.txt', 'w') as output_file:
    output_file.write("Election Results\n")
    output_file.write("-------------------------\n")
    output_file.write(f"Total Votes: {total_votes}\n")
    output_file.write("-------------------------\n")
    for candidate, votes in candidate_votes.items():
        percentage = round(vote_percentages[candidate], 3)
        output_file.write(f"{candidate}: {percentage}% ({votes})\n")
    output_file.write("-------------------------\n")
    output_file.write(f"Winner: {winner}\n")
    
