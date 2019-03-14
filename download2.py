from bs4 import BeautifulSoup
import numpy as np
import csv
import requests
import itertools, random

def into_words(row):#converts a row of HTML into text
    return [[j.contents[0] for j in i.find_all('a')] for i in row]

def parse(level):
    rows = level.find_all("div")
    
    for i in range(len(rows)):
        rows[i] = into_words(rows[i].find_all('div'))
    return [i for i in rows if i != []]

def download(year):
    r = requests.get("https://www.sports-reference.com/cbb/postseason/" + str(year) +"-ncaa.html")
    soup = BeautifulSoup(r.text, 'html.parser')
    rounds = soup.find_all("div", attrs = {"class":"round"})

    rounds_parsed = [parse(i) for i in rounds]#Gives us a list of data [[team1, score1], [team2, score2]]
    rounds_parsed = list(itertools.chain.from_iterable([i for i in rounds_parsed if len(i[0]) != 1])) #combines all matchups
    return rounds_parsed

def write(year):
    ok = download(year)
    with open("games/ncaa" + str(year) + "games.csv", "w",newline = "") as page:
        spamwriter = csv.writer(page, delimiter = ',')
        spamwriter.writerow(["Team_1", "Team_2", "Team_1_Score", "Team_2_Score", "Result"])
        for i in ok:
            v = random.randint(0, 1)
            add_this = i[0-v] + i[1-v]
            add_this[1], add_this[2] = add_this[2], add_this[1]
            spamwriter.writerow(add_this + [int(int(add_this[2]) > int(add_this[3]))])
    
