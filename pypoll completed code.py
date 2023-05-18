# Import modules
import csv
import os

# Create path for the election data
data_path = os.path.join('C:\\Users\\xhuli\\OneDrive\\Desktop\\Starter_Code\\PyPoll\\Resources\\election_data.csv')

# List for the names of candidate
candidate = {}

# Variables
#total number of votes
total_votes = 0
#capture the number of votes each candidate gets
vote_count = []
# determine winner
winner = ["",0]
# Percentage of total votes each candidate garners 
percent_votes = []

# Open the data set
with open(data_path) as elect_data:

    # Read the file
    csv_reader = csv.reader(elect_data, delimiter=",")
    header = next(csv_reader) 

    # Loop through the rows of the file
    for row in csv_reader:
        
        # Check if the candidate in the new row already exists 
        # If so, add 1 to their vote count
        if row[2] in candidate.keys():
            candidate[row[2]] +=1
        
        # Add remaining candidate in the dictionary if they are not in it 
        else:
            candidate[row[2]] = 1
    
    # Calculate total votes for each candidate
    for candidate in candidate.keys():
        total_votes = total_votes + candidate[candidate]

          # Check for the winner candidate
    for candidate in vote_count:
        if candidate[1] > winner[1]:
            winner = [candidate[0], candidate[1]]


    # Print election results

    print("\n")
    print("Election Results")
    print("----------------------------")
    print(f"Total Votes: {total_votes}")
    print("----------------------------")

    for candidate in vote_count:
        print(f"{candidate[0]}: {round(candidate[1]/total_votes * 100, 3)}% ({candidate[1]})")

    print("----------------------------")
    print(f"Winner: {winner[0]}")
    print("----------------------------")
    

result_path = os.path.join("analysis", "results.txt")

with open(result_path, 'w') as result_file:

    # Writes each line exactly how we printed in the terminal
    result_file.writelines(["Election Results \n",
   "---------------------------- \n",
    f"Total Votes: {total_votes} \n",
    "---------------------------- \n"])

    for cand in vote_count:
        result_file.write(f"{candidate[0]}: {round(candidate[1]/total_votes * 100, 3)}% ({candidate[1]}) \n")

    result_file.writelines(["---------------------------- \n",
    f"Winner: {winner[0]} \n",
    "---------------------------- \n"])