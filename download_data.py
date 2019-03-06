import urllib, requests
from bs4 import BeautifulSoup
import csv

ballteams = ['Abilene Christian', 'Air Force', 'Akron', 'Alabama A&M', 'Alabama-Birmingham', 'Alabama State', 'Alabama', 'Albany (NY)', 'Alcorn State', 'American', 'Appalachian State', 'Arizona State', 'Arizona', 'Little Rock', 'Arkansas-Pine Bluff', 'Arkansas State', 'Arkansas', 'Army', 'Auburn', 'Austin Peay', 'Ball State', 'Baylor', 'Belmont', 'Bethune-Cookman', 'Binghamton', 'Boise State', 'Boston College', 'Boston University', 'Bowling Green State', 'Bradley', 'Brigham Young', 'Brown', 'Bryant', 'Bucknell', 'Buffalo', 'Butler', 'Cal Poly', 'Cal State Bakersfield', 'Cal State Fullerton', 'Cal State Northridge', 'UC-Davis', 'UC-Irvine', 'UC-Riverside', 'UC-Santa Barbara', 'University of California', 'Campbell', 'Canisius', 'Central Arkansas', 'Central Connecticut State', 'Central Florida', 'Central Michigan', 'Charleston Southern', 'Charlotte', 'Chattanooga', 'Chicago State', 'Cincinnati', 'Citadel', 'Clemson', 'Cleveland State', 'Coastal Carolina', 'Colgate', 'College of Charleston', 'Colorado State', 'Colorado', 'Columbia', 'Connecticut', 'Coppin State', 'Cornell', 'Creighton', 'Dartmouth', 'Davidson', 'Dayton', 'Delaware State', 'Delaware', 'Denver', 'DePaul', 'Detroit Mercy', 'Drake', 'Drexel', 'Duke', 'Duquesne', 'East Carolina', 'East Tennessee State', 'Eastern Illinois', 'Eastern Kentucky', 'Eastern Michigan', 'Eastern Washington', 'Elon', 'Evansville', 'Fairfield', 'Fairleigh Dickinson', 'Florida A&M', 'Florida Atlantic', 'Florida Gulf Coast', 'Florida International', 'Florida State', 'Florida', 'Fordham', 'Fresno State', 'Furman', 'Gardner-Webb', 'George Mason', 'George Washington', 'Georgetown', 'Georgia Southern', 'Georgia State', 'Georgia Tech', 'Georgia', 'Gonzaga', 'Grambling', 'Grand Canyon', 'Green Bay', 'Hampton', 'Hartford', 'Harvard', 'Hawaii', 'High Point', 'Hofstra', 'Holy Cross', 'Houston Baptist', 'Houston', 'Howard', 'Idaho State', 'Idaho', 'Illinois-Chicago', 'Illinois State', 'Illinois', 'Incarnate Word', 'Indiana State', 'Indiana', 'Iona', 'Iowa State', 'Iowa', 'Purdue-Fort Wayne', 'IUPUI', 'Jackson State', 'Jacksonville State', 'Jacksonville', 'James Madison', 'Kansas State', 'Kansas', 'Kennesaw State', 'Kent State', 'Kentucky', 'La Salle', 'Lafayette', 'Lamar', 'Lehigh', 'Liberty', 'Lipscomb', 'Long Beach State', 'Long Island University', 'Longwood', 'Louisiana', 'Louisiana-Monroe', 'Louisiana State', 'Louisiana Tech', 'Louisville', 'Loyola (IL)', 'Loyola Marymount', 'Loyola (MD)', 'Maine', 'Manhattan', 'Marist', 'Marquette', 'Marshall', 'Maryland-Baltimore County', 'Maryland-Eastern Shore', 'Maryland', 'Massachusetts-Lowell', 'Massachusetts', 'McNeese State', 'Memphis', 'Mercer', 'Miami (FL)', 'Miami (OH)', 'Michigan State', 'Michigan', 'Middle Tennessee', 'Milwaukee', 'Minnesota', 'Mississippi State', 'Mississippi Valley State', 'Mississippi', 'Missouri-Kansas City', 'Missouri State', 'Missouri', 'Monmouth', 'Montana State', 'Montana', 'Morehead State', 'Morgan State', "Mount St. Mary's", 'Murray State', 'Navy', 'Omaha', 'Nebraska', 'Nevada-Las Vegas', 'Nevada', 'New Hampshire', 'New Mexico State', 'New Mexico', 'New Orleans', 'Niagara', 'Nicholls State', 'NJIT', 'Norfolk State', 'North Carolina-Asheville', 'North Carolina A&T', 'North Carolina Central', 'North Carolina-Greensboro', 'North Carolina State', 'North Carolina-Wilmington', 'North Carolina', 'North Dakota State', 'North Dakota', 'North Florida', 'North Texas', 'Northeastern', 'Northern Arizona', 'Northern Colorado', 'Northern Illinois', 'Northern Iowa', 'Northern Kentucky', 'Northwestern State', 'Northwestern', 'Notre Dame', 'Oakland', 'Ohio State', 'Ohio', 'Oklahoma State', 'Oklahoma', 'Old Dominion', 'Oral Roberts', 'Oregon State', 'Oregon', 'Pacific', 'Penn State', 'Pennsylvania', 'Pepperdine', 'Pittsburgh', 'Portland State', 'Portland', 'Prairie View', 'Presbyterian', 'Princeton', 'Providence', 'Purdue', 'Quinnipiac', 'Radford', 'Rhode Island', 'Rice', 'Richmond', 'Rider', 'Robert Morris', 'Rutgers', 'Sacramento State', 'Sacred Heart', 'Saint Francis (PA)', "Saint Joseph's", 'Saint Louis', "Saint Mary's (CA)", "Saint Peter's", 'Sam Houston State', 'Samford', 'San Diego State', 'San Diego', 'San Francisco', 'San Jose State', 'Santa Clara', 'Savannah State', 'Seattle', 'Seton Hall', 'Siena', 'South Alabama', 'South Carolina State', 'South Carolina Upstate', 'South Carolina', 'South Dakota State', 'South Dakota', 'South Florida', 'Southeast Missouri State', 'Southeastern Louisiana', 'Southern California', 'SIU Edwardsville', 'Southern Illinois', 'Southern Methodist', 'Southern Mississippi', 'Southern Utah', 'Southern', 'St. Bonaventure', 'St. Francis (NY)', "St. John's (NY)", 'Stanford', 'Stephen F. Austin', 'Stetson', 'Stony Brook', 'Syracuse', 'Temple', 'Tennessee-Martin', 'Tennessee State', 'Tennessee Tech', 'Tennessee', 'Texas A&M-Corpus Christi', 'Texas A&M', 'Texas-Arlington', 'Texas Christian', 'Texas-El Paso', 'Texas-Rio Grande Valley', 'Texas-San Antonio', 'Texas Southern', 'Texas State', 'Texas Tech', 'Texas', 'Toledo', 'Towson', 'Troy', 'Tulane', 'Tulsa', 'UCLA', 'Utah State', 'Utah Valley', 'Utah', 'Valparaiso', 'Vanderbilt', 'Vermont', 'Villanova', 'Virginia Commonwealth', 'VMI', 'Virginia Tech', 'Virginia', 'Wagner', 'Wake Forest', 'Washington State', 'Washington', 'Weber State', 'West Virginia', 'Western Carolina', 'Western Illinois', 'Western Kentucky', 'Western Michigan', 'Wichita State', 'William & Mary', 'Winthrop', 'Wisconsin', 'Wofford', 'Wright State', 'Wyoming', 'Xavier', 'Yale', 'Youngstown State']
pomteams = ['Abilene Christian', 'Air Force', 'Akron', 'Alabama', 'Alabama A&M', 'Alabama St.', 'Albany', 'Alcorn St.', 'American', 'Appalachian St.', 'Arizona', 'Arizona St.', 'Arkansas', 'Arkansas-Pine Bluff', 'Arkansas St.', 'Army', 'Auburn', 'Austin Peay', 'Ball St.', 'Baylor', 'Belmont', 'Bethune Cookman', 'Binghamton', 'Boise St.', 'Boston College', 'Boston University', 'Bowling Green', 'Bradley', 'Brown', 'Bryant', 'Bucknell', 'Buffalo', 'Butler', 'Brigham Young', 'Cal Poly', 'Cal St. Bakersfield', 'Cal St. Fullerton', 'Cal St. Northridge', 'University of California', 'Campbell', 'Canisius', 'Central Arkansas', 'Central Connecticut', 'Central Michigan', 'Charleston Southern', 'Charlotte', 'Chattanooga', 'Chicago St.', 'Cincinnati', 'Clemson', 'Cleveland St.', 'Coastal Carolina', 'Colgate', 'College of Charleston', 'Colorado', 'Colorado St.', 'Columbia', 'Connecticut', 'Coppin St.', 'Cornell', 'Creighton', 'Dartmouth', 'Davidson', 'Dayton', 'Delaware', 'Delaware St.', 'Denver', 'DePaul', 'Detroit', 'Drake', 'Drexel', 'Duke', 'Duquesne', 'East Carolina', 'East Tennessee St.', 'Eastern Illinois', 'Eastern Kentucky', 'Eastern Michigan', 'Eastern Washington', 'Elon', 'Evansville', 'Fairfield', 'Fairleigh Dickinson', 'Florida International', 'Florida', 'Florida A&M', 'Florida Atlantic', 'Florida Gulf Coast', 'Florida St.', 'Fordham', 'Purdue-Fort Wayne', 'Fresno St.', 'Furman', 'Gardner Webb', 'George Mason', 'George Washington', 'Georgetown', 'Georgia', 'Georgia Southern', 'Georgia St.', 'Georgia Tech', 'Gonzaga', 'Grambling St.', 'Grand Canyon', 'Green Bay', 'Hampton', 'Hartford', 'Harvard', 'Hawaii', 'High Point', 'Hofstra', 'Holy Cross', 'Houston', 'Houston Baptist', 'Howard', 'Idaho', 'Idaho St.', 'Illinois', 'Illinois-Chicago', 'Illinois St.', 'Incarnate Word', 'Indiana', 'Indiana St.', 'Iona', 'Iowa', 'Iowa St.', 'IUPUI', 'Jackson St.', 'Jacksonville', 'Jacksonville St.', 'James Madison', 'Kansas', 'Kansas St.', 'Kennesaw St.', 'Kent St.', 'Kentucky', 'La Salle', 'Lafayette', 'Lamar', 'Lehigh', 'Liberty', 'Lipscomb', 'Little Rock', 'Long Island University', 'Long Beach St.', 'Longwood', 'Louisiana', 'Louisiana-Monroe', 'Louisiana Tech', 'Louisville', 'Loyola Chicago', 'Loyola Marymount', 'Loyola MD', 'Louisiana State', 'Maine', 'Manhattan', 'Marist', 'Marquette', 'Marshall', 'Maryland', 'Maryland Eastern Shore', 'Massachusetts', 'McNeese St.', 'Memphis', 'Mercer', 'Miami FL', 'Miami OH', 'Michigan', 'Michigan St.', 'Middle Tennessee', 'Milwaukee', 'Minnesota', 'Mississippi', 'Mississippi St.', 'Mississippi Valley St.', 'Missouri', 'Missouri St.', 'Monmouth', 'Montana', 'Montana St.', 'Morehead St.', 'Morgan St.', "Mount St. Mary's", 'Murray St.', 'Navy', 'Nebraska', 'Omaha', 'Nevada', 'New Hampshire', 'New Mexico', 'New Mexico St.', 'New Orleans', 'Niagara', 'Nicholls St.', 'NJIT', 'Norfolk St.', 'North Carolina', 'North Carolina A&T', 'North Carolina Central', 'North Carolina St.', 'North Dakota', 'North Dakota St.', 'North Florida', 'North Texas', 'Northeastern', 'Northern Arizona', 'Northern Colorado', 'Northern Illinois', 'Northern Iowa', 'Northern Kentucky', 'Northwestern', 'Northwestern St.', 'Notre Dame', 'Oakland', 'Ohio', 'Ohio St.', 'Oklahoma', 'Oklahoma St.', 'Old Dominion', 'Oral Roberts', 'Oregon', 'Oregon St.', 'Pacific', 'Pennsylvania', 'Penn St.', 'Pepperdine', 'Pittsburgh', 'Portland', 'Portland St.', 'Prairie View A&M', 'Presbyterian', 'Princeton', 'Providence', 'Purdue', 'Quinnipiac', 'Radford', 'Rhode Island', 'Rice', 'Richmond', 'Rider', 'Robert Morris', 'Rutgers', 'Sacramento St.', 'Sacred Heart', "Saint Joseph's", 'Saint Louis', "Saint Mary's", "Saint Peter's", 'Sam Houston St.', 'Samford', 'San Diego', 'San Diego St.', 'San Francisco', 'San Jose St.', 'Santa Clara', 'Savannah St.', 'Seattle', 'Seton Hall', 'Siena', 'SIU Edwardsville', 'Southern Methodist', 'South Alabama', 'South Carolina', 'South Carolina St.', 'South Dakota', 'South Dakota St.', 'South Florida', 'Southeast Missouri St.', 'Southeastern Louisiana', 'Southern', 'Southern Illinois', 'Southern Miss', 'Southern Utah', 'St. Bonaventure', 'St. Francis NY', 'Saint Francis PA', "St. John's", 'Stanford', 'Stephen F. Austin', 'Stetson', 'Stony Brook', 'Syracuse', 'Texas Christian', 'Temple', 'Tennessee', 'Tennessee-Martin', 'Tennessee St.', 'Tennessee Tech', 'Texas', 'Texas A&M', 'Texas A&M Corpus Chris', 'Texas Southern', 'Texas St.', 'Texas Tech', 'Citadel', 'Toledo', 'Towson', 'Troy', 'Tulane', 'Tulsa', 'Alabama-Birmingham', 'UC Davis', 'UC Irvine', 'UC Riverside', 'UC Santa Barbara', 'Central Florida', 'UCLA', 'Massachusetts-Lowell', 'Maryland Baltimore County', 'Missouri-Kansas City', 'North Carolina-Asheville', 'North Carolina-Greensboro', 'North Carolina-Wilmington', 'Nevada-Las Vegas', 'Southern California', 'South Carolina Upstate', 'Texas-Arlington', 'Texas-Rio Grande Valley', 'Utah', 'Utah St.', 'Utah Valley', 'Texas-El Paso', 'Texas-San Antonio', 'Valparaiso', 'Vanderbilt', 'Virginia Commonwealth', 'Vermont', 'Villanova', 'Virginia', 'Virginia Tech', 'VMI', 'Wagner', 'Wake Forest', 'Washington', 'Washington St.', 'Weber St.', 'West Virginia', 'Western Carolina', 'Western Illinois', 'Western Kentucky', 'Western Michigan', 'Wichita St.', 'William & Mary', 'Winthrop', 'Wisconsin', 'Wofford', 'Wright St.', 'Wyoming', 'Xavier', 'Yale', 'Youngstown St.']

ballteams.sort()
pomteams.sort()
#Returns table heading
def heading(file):
    name_box = file.find('thead').find_all('tr')
    return [i.contents[0] if i.contents[0] != '\xa0' else "" for i in name_box[1].find_all('th')  ][1:]


#Returns school name, returns None if invalid row
def get_school(row):
    k = row.find('td',attrs= {'class':'left'})
    if k == None:
        return None
    return k.find('a').contents[0]

#Returns the row of data
#Precondition: Valid row
def get_fields(row):
    k = row.find_all("td",attrs = {'class':'right'})
    return [get_school(row)] + [i.contents[0] if len(i.contents) != 0 else "" for i in k]


def write_year(year):
    #downloads HTML
    r = requests.get("https://www.sports-reference.com/cbb/seasons/" + str(year) + "-advanced-school-stats.html")

    #Parses HTML
    soup = BeautifulSoup(r.text,'html.parser')

    #Goes to the <tbody> section of the code
    name_box = soup.find('tbody')
    #List of all the <tr> within the <tbody>
    array = name_box.find_all('tr')

    #Python code to write to a CSV
    with open("ncaa" + str(year) + ".csv", "w",newline = "") as page:
        spamwriter = csv.writer(page, delimiter = ',')
        spamwriter.writerow(heading(soup))
        for i in array:
            if get_school(i):
                spamwriter.writerow(get_fields(i))
    

#Creates .csv from 2000 to 2017
def generate():
    for i in range(2000, 2018):
        write_year(i)
        print(i, "done")



pom2ref = {'Arkansas Little Rock':'Little Rock','Alabama St.': 'Alabama State', 'UAB': 'Alabama-Birmingham', 'Albany': 'Albany (NY)', 'Alcorn St.': 'Alcorn State', 'Appalachian St.': 'Appalachian State', \
           'Arizona St.': 'Arizona State', 'Arkansas St. ': 'Arkansas State', 'Arkansas Pine Bluff': 'Arkansas-Pine Bluff', 'Ball St.': 'Ball State', 'Bethune Cookman': 'Bethune-Cookman', \
           'Boise St.': 'Boise State', 'Bowling Green': 'Bowling Green State', 'BYU': 'Brigham Young', 'Cal St. Bakersfield': 'Cal State Bakersfield', 'Cal St. Fullerton': 'Cal State Fullerton', \
           'Cal St. Northridge': 'Cal State Northridge', 'Central Connecticut': 'Central Connecticut State', 'UCF': 'Central Florida', 'Chicago St.': 'Chicago State', 'The Citadel': 'Citadel', \
           'Cleveland St.': 'Cleveland State', 'Colorado St.': 'Colorado State', 'Coppin St.': 'Coppin State', 'Delaware St.': 'Delaware State', 'Detroit': 'Detroit Mercy', \
           'East Tennessee St.': 'East Tennessee State', 'FIU': 'Florida International', 'Florida St.': 'Florida State', 'Fresno St.': 'Fresno State', 'Gardner Webb': 'Gardner-Webb', \
           'Georgia St.': 'Georgia State', 'Grambling St.': 'Grambling', 'Idaho St.': 'Idaho State', 'Illinois St.': 'Illinois State', 'Illinois Chicago': 'Illinois-Chicago', 'Indiana St.': 'Indiana State',\
           'Iowa St.': 'Iowa State', 'Jackson St.': 'Jackson State', 'Jacksonville St.': 'Jacksonville State', 'Kansas St.': 'Kansas State', 'Kennesaw St.': 'Kennesaw State', 'Kent St.': 'Kent State',\
           'Long Beach St.': 'Long Beach State', 'LIU Brooklyn': 'Long Island University', 'Louisiana Lafayette': 'Louisiana', 'LSU': 'Louisiana State', 'Louisiana Monroe': 'Louisiana-Monroe', \
           'Loyola Chicago': 'Loyola (IL)', 'Loyola MD': 'Loyola (MD)', 'UMBC': 'Maryland-Baltimore County', 'Maryland Eastern Shore': 'Maryland-Eastern Shore', 'UMass Lowell': 'Massachusetts-Lowell',\
           'McNeese St.': 'McNeese State', 'Miami FL': 'Miami (FL)', 'Miami OH': 'Miami (OH)', 'Michigan St.': 'Michigan State', 'Mississippi St.': 'Mississippi State', \
           'Mississippi Valley St.': 'Mississippi Valley State', 'Missouri St.': 'Missouri State', 'UMKC': 'Missouri-Kansas City', 'Montana St.': 'Montana State', 'Morehead St.': 'Morehead State', \
           'Morgan St.': 'Morgan State', 'Murray St.': 'Murray State', 'UNLV': 'Nevada-Las Vegas', 'New Mexico St.': 'New Mexico State', 'Nicholls St.': 'Nicholls State', 'Norfolk St.': 'Norfolk State', \
           'North Carolina St.': 'North Carolina State', 'UNC Asheville': 'North Carolina-Asheville', 'UNC Greensboro': 'North Carolina-Greensboro', 'UNC Wilmington': 'North Carolina-Wilmington', \
           'North Dakota St.': 'North Dakota State', 'Northwestern St.': 'Northwestern State', 'Ohio St.': 'Ohio State', 'Oklahoma St.': 'Oklahoma State', 'Nebraska Omaha': 'Omaha', 'Oregon St.': 'Oregon State',\
           'Penn St.': 'Penn State', 'Penn': 'Pennsylvania', 'Portland St.': 'Portland State', 'Prairie View A&M': 'Prairie View', 'IPFW':'Fort Wayne','Fort Wayne': 'Purdue-Fort Wayne', 'Sacramento St.': 'Sacramento State',\
           'St. Francis PA': 'Saint Francis (PA)', "Saint Mary's": "Saint Mary's (CA)", 'Sam Houston St.': 'Sam Houston State', 'San Diego St.': 'San Diego State', 'San Jose St.': 'San Jose State', \
           'Savannah St.': 'Savannah State', 'South Carolina St.': 'South Carolina State', 'USC Upstate': 'South Carolina Upstate', 'South Dakota St.': 'South Dakota State', \
           'Southeast Missouri St.': 'Southeast Missouri State', 'USC': 'Southern California', 'SMU': 'Southern Methodist', 'Southern Miss': 'Southern Mississippi', 'St. Francis NY': 'St. Francis (NY)', \
           "St. John's": "St. John's (NY)", 'Tennessee St.': 'Tennessee State', 'Tennessee Martin': 'Tennessee-Martin', 'Texas A&M Corpus Chris': 'Texas A&M-Corpus Christi', 'TCU': 'Texas Christian', \
           'Texas St.': 'Texas State', 'UT Arlington': 'Texas-Arlington', 'UTEP': 'Texas-El Paso', 'Troy St.':"Troy",'UT Rio Grande Valley': 'Texas-Rio Grande Valley', 'UTSA': 'Texas-San Antonio', 'UC Davis': 'UC-Davis', \
           'UC Irvine': 'UC-Irvine', 'UC Riverside': 'UC-Riverside', 'UC Santa Barbara': 'UC-Santa Barbara', 'California': 'University of California', 'Utah St.': 'Utah State', \
           'VCU': 'Virginia Commonwealth', 'Washington St.': 'Washington State','Weber St.': 'Weber State', 'Wichita St.': 'Wichita State', 'Wright St.': 'Wright State', 'Youngstown St.': 'Youngstown State'}


head = ['School', 'G', 'W', 'L', 'W-L%', 'SRS', 'SOS', 'W', 'L', 'W', 'L', 'W', 'L', 'Tm.', 'Opp.', '', 'Pace', 'ORtg', 'FTr', '3PAr', 'TS%', 'TRB%', 'AST%', 'STL%', 'BLK%', 'eFG%', 'TOV%', 'ORB%', 'FT/FGA','AdjEM', 'AdjO', 'AdjD', 'AdjT', 'Luck', 'SOS AdjEM', 'OppO','OppD','NCSOS AdjEM']

replace = lambda x: pom2ref[x] if x in pom2ref else x
def pom_school(row):
    k = row.find('td',attrs= {'class':'next_left'})
    if k == None:
        return None
    return replace(k.find('a').contents[0])

def ken_row(row):
    k = row.find_all('td')#attrs= {'class':'next_left'})
    if k == None:
        return None
    return [i.contents[0] for i in k if i.find('span') == None][-9:]

def pom(year):
    r = requests.get("https://kenpom.com/index.php?y="  + str(year) + "&s=TeamName")
    soup = BeautifulSoup(r.text, 'html.parser')
    array = soup.find('tbody').find_all('tr')
    u = []
    for i in array:
        j = pom_school(i)
        if j:
            u.append([j] + ken_row(i))
    return sorted(u)

def bball(year):
    r = requests.get("https://www.sports-reference.com/cbb/seasons/" + str(year) + "-advanced-school-stats.html")

    #Parses HTML
    soup = BeautifulSoup(r.text,'html.parser')

    #Goes to the <tbody> section of the code
    name_box = soup.find('tbody')
    #List of all the <tr> within the <tbody>
    array = name_box.find_all('tr')
    u = []
    index = 0
    for i in array:
        if get_school(i):
            u.append(get_fields(i))

    u = sorted(u, key = lambda x: x[0])
    return u





def output(year):
    u = bball(year)
    names = set([i[0] for i in u])

    v = pom(year)
    #deleted = list(filter(lambda x: x[0] not in names,  v))
    #print([i[0] for i in deleted])
    v = list(filter(lambda x: x[0] in names,  v))           
    vnames = set([i[0] for i in v])
    #deleted2 = list(filter(lambda x: x[0] not in vnames,  u))
    #print([i[0] for i in deleted2])
    u = list(filter(lambda x: x[0] in vnames, u))
    w = [u[i] + v[i][1:] for i in range(len(u))]

    with open("ncaa" + str(year) + ".csv", "w",newline = "") as page:
        spamwriter = csv.writer(page, delimiter = ',')
        spamwriter.writerow(head)
        for i in w:
            spamwriter.writerow(i)
    
