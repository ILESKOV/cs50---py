import csv
import sys
import random

# Number of simulations to run
N = 10


def main():
    # Ensure correct usage
    if len(sys.argv) != 2:
        sys.exit("Usage: python tournament.py FILENAME")

    teams = []
    with open(sys.argv[1], 'r') as f:
        reader = csv.DictReader(f)  # create a csv reader object
        for row in reader:  # iterate through each row in the csv file
            row['rating'] = int(row['rating'])  # convert the rating column to an integer
            teams.append(row)  # add the row to the teams list

    counts = {}
    for i in range(N):  # iterate through the number of simulations
        winner = simulate_tournament(teams)  # simulate a tournament and get the winner
        if winner in counts:  # if the winner is already in the counts dictionary
            counts[winner] += 1  # increment its count
        else:  # otherwise
            counts[winner] = 1  # add it to the dictionary with a count of 1

    # Print the results
    for team in sorted(counts, key=lambda x: counts[x], reverse=True):
        # Sort the dictionary by count in descending order and iterate through each team
        # Print the team name and its chance of winning (count divided by the number of simulations)
        print(f"{team}: {counts[team] / N:.1%} chance of winning")


def simulate_game(team1, team2):
    """Simulate a game. Return True if team1 wins, False otherwise."""
    rating1 = team1["rating"]  # get the rating of team1
    rating2 = team2["rating"]  # get the rating of team2
    probability = 1 / (1 + 10 ** ((rating2 - rating1) / 600))  # calculate the win probability
    return random.random() < probability  # return True if a random number is less than the probability, False otherwise


def simulate_round(teams):
    """Simulate a round. Return a list of winning teams."""
    winners = []
    for i in range(0, len(teams), 2):  # iterate through every other team in the list
        if simulate_game(teams[i], teams[i + 1]):  # simulate a game between the two teams
            winners.append(teams[i])  # add the winner to the winners list
        else:
            winners.append(teams[i + 1])  # add the other team to the winners list
    return winners  # return the list of winners


def simulate_tournament(teams):
    """Simulate a tournament. Return name of winning team."""
    while len(teams) > 1:  # while there is more than one team left in the tournament
        teams = simulate_round(teams)  # simulate a round and get the winners
    return teams[0]['team']  # return the name of the winning team


if __name__ == "__main__":
    main()
