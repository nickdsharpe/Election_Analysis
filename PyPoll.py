import csv
import os

# Assign variables for load and save file
file_to_load = 'election_results.csv'
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open election results and save the file
with open(file_to_load) as election_data:

    # Read the file object with the reader function
    file_reader = csv.reader(election_data)

    # Print the header row
    headers = next(file_reader)

    print(headers)
    

# 1. Total number of votes cast
# 2. Complete list of candidates who recieved votes
# 3. Percentage of votes each candidate won
# 4. Total number of votes each candidate won
# 5. Winner of election based on popular vote
