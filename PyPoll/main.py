import csv
import os

# Open the csv file
csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath, newline='') as csvfile:
    election_data = csv.reader(csvfile, delimiter=',')

    # Skipping the first line
    csv_header = next(election_data)

    # Variables
    total_votes = 0

    # dictionary to store Candidate names and votes {name:votes}
    candidates = {}

    winner = []

    for row in election_data:

        # The total number of votes cast
        total_votes = total_votes + 1

        # A complete list of candidates who received votes
        # and
        # The total number of votes each candidate won
        candidate = row[2]
        if candidate not in candidates.keys():
            candidates[row[2]] = 1

        elif candidate in candidates.keys():
            candidates[row[2]] = candidates[row[2]] + 1

    # The percentage of votes each candidate won

    for candidate in candidates.keys():
        percent_votes = "{0:.3f}".format((candidates[candidate] / total_votes) * 100)

        # Nesting the candidates{} and the percent votes:
        # ({candidate: {"Votes": candidate_votes, "Percent Votes: percent_votes"}}
        candidates[candidate] = {"votes": candidates[candidate], "Percent Votes": percent_votes}

# The winner of the election based on popular vote.
# Descent candidates names sorted through dictionary by popular vote.
winner = sorted(candidates, key=lambda x: (candidates[x]["votes"]), reverse=True)

# Creating an array with the results
array_results = []


def results():
    for cand in winner:
        array_results.append(f"{cand}: {candidates[cand]['Percent Votes']}% ({candidates[cand]['votes']})")
    return array_results

results()


# Print the results

print(f"Election Results\n"
      f"-------------------------\n"
      f"Total Votes: {total_votes}\n"
      f"-------------------------")
for line in array_results:
    print(line)
print(f"-------------------------\n"
      f"Winner: {winner[0]}\n"
      f"-------------------------")

# Export a text file with the results
output_path = os.path.join("election_results.txt")
with open(output_path, 'w') as txtfile:
    txtfile.write("Election Results\n"
                  f"-------------------------\n"
                  f"Total Votes: {total_votes}\n"
                  f"-------------------------\n")
    for line in array_results:
        txtfile.write(f"{line}\n")
    txtfile.write(f"-------------------------\n"
                  f"Winner: {winner[0]}\n"
                  f"-------------------------")
