from bs4 import BeautifulSoup
import numpy as np
import csv
import requests

games_per_round = [8, 4, 2, 1]
final_four_games = [2, 1]
regions = ['west', 'midwest', 'south', 'east']


def parse_region(region_html, num_games, year):
    rounds = region_html.find_all(class_='round')

    # for each round
    for c in range(0, len(num_games)):

        # get HTML for specific round
        round = rounds[c]

        # get all team HTML
        teams = round.find_all('div')

        #iterate through all games
        for i in range(0, num_games[c]):
            #find 
            data = teams[3 * i].find_all('a')
            team1 = data[0].get_text()
            team1_score = data[1].get_text()
            team2 = data[2].get_text()
            team2_score = data[3].get_text()
            #print("Team 1: %s, Team 2: %s, %s-%s" % (team1, team2, team1_score, team2_score))
            if int(team1_score) < int(team2_score):
                winner = team2
                loser = team1
                win_score = team2_score
                lose_score = team1_score
            else:
                winner = team2
                loser = team1
                win_score = team2_score
                lose_score = team1_score

            rand = np.random.randint(0, 2)
            if rand:
                toWrite = [winner, loser, win_score, lose_score, 1]
            else:
                toWrite = [loser, winner, lose_score, win_score, 0]


            with open("games/ncaa" + str(year) + "games.csv", "a", newline="") as page:
                spamwriter = csv.writer(page, delimiter=',')
                spamwriter.writerow(toWrite)

def write_year(year):
    r = requests.get("https://www.sports-reference.com/cbb/postseason/" + str(year) + "-ncaa.html")
    soup = BeautifulSoup(r.text, 'html.parser')

    with open("games/ncaa" + str(year) + "games.csv", "w",newline = "") as page:
        spamwriter = csv.writer(page, delimiter = ',')
        spamwriter.writerow(["Team_1", "Team_2", "Team_1_Score", "Team_2_Score", "Result"])
    for i in range(0, len(regions)):
        region = soup.find(id=regions[i])
        parse_region(region, games_per_round, year)

    final_four = soup.find(id="national")
    parse_region(final_four, final_four_games, year)


def generate():
    for i in range(2012, 2019):
        write_year(i)
        print(i, "done")


generate()