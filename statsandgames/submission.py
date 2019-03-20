import csv

j = {}
conversion = {"UNC Greensboro": "North Carolina-Greensboro", "UNC":"North Carolina","Penn":"Pennsylvania",\
              "NC State": "North Carolina State","TCU":"Texas Christian","UMBC":"Maryland-Baltimore County",\
              "VA Commonwealth":"Virginia Commonwealth","Saint Mary's":"Saint Mary's (CA)","UNC Wilmington":"North Carolina-Wilmington",\
              "ETSU":"East Tennessee State","USC":"Southern California","SMU":"Southern Methodist",\
              "St. Joseph's":"Saint Joseph's","UConn":"Connecticut","California":"University of California",\
              "UNC Asheville":"North Carolina-Asheville","Pitt":"Pittsburgh","Ole Miss":"Mississippi",\
              "LSU":"Louisiana State",'BYU':"Brigham Young",'UMass':"Massachusetts","UNLV":"Nevada-Las Vegas",\
              "LIU-Brooklyn":"Long Island University","Detroit":"Detroit Mercy","Southern Miss":"Southern Mississippi",\
              "Texas A&M;":"Texas A&M","North Carolina A&T;":"North Carolina A&T"}

with open('Teams.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter = ',')
    for i in readCSV:
        if i[1] in conversion:
            j[conversion[i[1]]] = i[0]
        else:
            j[i[1]] = i[0]


