from bs4 import BeautifulSoup
import numpy as np
import csv
import requests

games_per_round = [8, 4, 2, 1]
regions = ['west', 'midwest', 'south', 'east']

"""TODO 
-Parse Final Four
-Insert into CSV
-Figure the """
def parse_region(region_html, num_games):
    rounds = region_html.find_all(class_='round')
    for c in range(0, len(num_games)):
        round = rounds[c]
        teams = round.find_all('div')
        for i in range(0, num_games[c]):
            data = teams[3 * i].find_all('a')
            team1 = data[0].get_text()
            team1_score = data[1].get_text()
            team2 = data[2].get_text()
            team2_score = data[3].get_text()
            print("Team 1: %s, Team 2: %s, %s-%s" % (team1, team2, team1_score, team2_score))

def write_year(year):
    r = requests.get("https://www.sports-reference.com/cbb/postseason/" + str(year) + "-ncaa.html")
    soup = BeautifulSoup(r.text, 'html.parser')
    for i in range(0, len(regions)):
        region = soup.find(id=regions[i])
        parse_region(region, games_per_round)



write_year(2018)