import urllib, requests
import csv


#Different names within sports reference
conversion = {"UNC Greensboro": "North Carolina-Greensboro", "UNC":"North Carolina","Penn":"Pennsylvania",\
              "NC State": "North Carolina State","TCU":"Texas Christian","UMBC":"Maryland-Baltimore County",\
              "VCU":"Virginia Commonwealth","Saint Mary's":"Saint Mary's (CA)","UNC Wilmington":"North Carolina-Wilmington",\
              "ETSU":"East Tennessee State","USC":"Southern California","SMU":"Southern Methodist",\
              "St. Joseph's":"Saint Joseph's","UConn":"Connecticut","California":"University of California",\
              "UNC Asheville":"North Carolina-Asheville","Pitt":"Pittsburgh","Ole Miss":"Mississippi",\
              "LSU":"Louisiana State",'BYU':"Brigham Young",'UMass':"Massachusetts","UNLV":"Nevada-Las Vegas",\
              "LIU-Brooklyn":"Long Island University","Detroit":"Detroit Mercy","Southern Miss":"Southern Mississippi",\
              "Texas A&M;":"Texas A&M","North Carolina A&T;":"North Carolina A&T","UCSB":"UC-Santa Barbara",\
              "UTSA":"Texas-San Antonio","St. Peter's":"Saint Peter's",'UTEP':"Texas-El Paso",\
              "Central Connecticut":"Central Connecticut State","UCF":"Central Florida",\
              "UIC":"Illinois-Chicago"}


location = lambda array, word: array[[i[0] for i in array].index(word)][1:]
rename = lambda x: conversion[x] if x in conversion else x
head = ['G1', 'W1', 'L1', 'W-L%1', 'SRS1', 'SOS1', 'ConfW1', 'ConfL1', 'HomeW1', 'HomeL1', 'AwayW1', 'AwayL1', 'Tm.1', 'Opp.1', 'MP1', 'FG1', 'FGA1', 'FG%1', '3P1', '3PA1', '3P%1', 'FT1', 'FTA1', 'FT%1', 'ORB1', 'TRB1', 'AST1', 'STL1', 'BLK1', 'TOV1', 'PF1', 'Pace1', 'ORtg1', 'FTr1', '3PAr1', 'TS%1', 'TRB%1', 'AST%1', 'STL%1', 'BLK%1', 'eFG%1', 'TOV%1', 'ORB%1', 'FT/FGA1', 'AdjEM1', 'AdjO1', 'AdjD1', 'AdjT1', 'Luck1', 'SOS AdjEM1', 'OppO1', 'OppD1', 'NCSOS AdjEM1', 'G2', 'W2', 'L2', 'W-L%2', 'SRS2', 'SOS2', 'ConfW2', 'ConfL2', 'HomeW2', 'HomeL2', 'AwayW2', 'AwayL2', 'Tm.2', 'Opp.2', 'MP2', 'FG2', 'FGA2', 'FG%2', '3P2', '3PA2', '3P%2', 'FT2', 'FTA2', 'FT%2', 'ORB2', 'TRB2', 'AST2', 'STL2', 'BLK2', 'TOV2', 'PF2', 'Pace2', 'ORtg2', 'FTr2', '3PAr2', 'TS%2', 'TRB%2', 'AST%2', 'STL%2', 'BLK%2', 'eFG%2', 'TOV%2', 'ORB%2', 'FT/FGA2', 'AdjEM2', 'AdjO2', 'AdjD2', 'AdjT2', 'Luck2', 'SOS AdjEM2', 'OppO2', 'OppD2', 'NCSOS AdjEM2']
def creation(year):

    #Downloads year's stats"
    stats = []
    with open('ncaa' + str(year) + '.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        stats = list(readCSV)

    #Reads in this year's games and finds corresponding stats
    solution = []
    with open('ncaa' + str(year) + 'games.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        heading = list(readCSV)[1:]
        for i in heading:
            solution.append([rename(i[0])] + [rename(i[1])] + i[2:] + location(stats, rename(i[0])) + location(stats, rename(i[1])))
            
    #Writes games + stats
    with open("ncaa" + str(year) + "gamesdata.csv",'w',newline = "") as page:
        spamwriter = csv.writer(page, delimiter = ',')
        spamwriter.writerow(["Team1","Team2","Points1","Points2","Result"] + head)
        for i in solution:
            spamwriter.writerow(i)
           

