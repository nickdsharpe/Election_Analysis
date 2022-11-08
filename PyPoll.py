import csv
import os

# Assign variables for load and save file
file_to_load = 'election_results.csv'
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize total vote counter
total_votes = 0
candidate_options = []
candidate_votes = {}

winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open election results and save the file
with open(file_to_load) as election_data:

    # Read the file object with the reader function
    file_reader = csv.reader(election_data)

    # Read the header row
    headers = next(file_reader)

    # Increment total votes
    for row in file_reader:

        total_votes += 1

        candidate_name = row[2]
       
        if candidate_name not in candidate_options:
            
            candidate_options.append(candidate_name)

            candidate_votes[candidate_name] = 0

        candidate_votes[candidate_name] += 1

# Save results to text file

with open(file_to_save, "w") as txt_file:

    # Print final votes to terminal
    election_results = (
        f"\nElection Results\n"
        f"-----------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-----------------------\n")

    print(election_results, end="")

    # Save final vote count to the text file
    txt_file.write(election_results)
    
    # Retrieve vote count and percentage

    for candidate_name in candidate_votes:

        votes = candidate_votes[candidate_name]

        vote_percentage = float(votes) / float(total_votes) * 100

        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidtes, vote count, and percentage to the terminal
        print(candidate_results)

        # Save canidate results to the text file
        txt_file.write(candidate_results)

        if (votes > winning_count) and (vote_percentage > winning_percentage):

            winning_count = votes

            winning_percentage = vote_percentage

            winning_candidate = candidate_name
        
    winning_candidate_summary = (

        f"--------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"---------------------------\n")
        
    print(winning_candidate_summary)

    # Save winning candidate results to text file
    txt_file.write(winning_candidate_summary)

            



