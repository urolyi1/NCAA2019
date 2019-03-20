import urllib, requests
from bs4 import BeautifulSoup
import csv

#plan: Match the teams by SRS, SOS and WL%
#Reasoning? We changed the names


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


def gf2(row):
    a = [i.contents[0] if i.contents != [] else '' for i in row.find_all('td')]
    if a == []:
        return []
    bas2ref = {'California-Irvine':'UC-Irvine','Louisiana-Lafayette':"Louisiana","Arkansas-Little Rock":"Little Rock"}
    a[1] = a[1].contents[0]
    if a[1] in bas2ref:
        a[1] = bas2ref[a[1]]
    return a[1:]

def create_year(year):
    #downloads HTML
    r = requests.get("https://web.archive.org/web/20160316031341/http://www.sports-reference.com/cbb/seasons/2016-school-stats.html")
    #Parses HTML
    soup = BeautifulSoup(r.text,'html.parser')

    #Goes to the <tbody> section of the code
    name_box = soup.find('tbody')
    #List of all the <tr> within the <tbody>
    array = name_box.find_all('tr')
    answer =[['School', 'G', 'W', 'L', 'W-L%', 'SRS', 'SOS', 'ConfW', 'ConfL', 'HomeW', 'HomeL', 'AwayW', 'AwayL', 'Tm.', 'Opp.', 'MP', 'FG', 'FGA', 'FG%', '3P', '3PA', '3P%', 'FT', 'FTA', 'FT%', 'ORB', 'TRB', 'AST', 'STL', 'BLK', 'TOV', 'PF']]
    #Python code to write to a CSV
    for i in array:
        j = gf2(i)
        if j != []:
#            j = j[:16] + [0] + j[16:]
            answer.append(j)

    return answer


def read_in(year):

    #Downloads year's stats"
    stats = []
    with open('ncaa' + str(year) + '.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        stats = list(readCSV)
    return stats

def formula(array1, array2):
    v = array1[:15] + array2[1:] + array1[15:]
    return v

def put_in(year):
    reader = read_in(year)
    reader = [i[:15] + i[16:] for i in reader]
    elementary = create_year(year)
    print(elementary[0])
    elementary = [i[:1] + i[16:] for i in elementary]
    print(elementary[0])
    new_one = [formula(reader[0], elementary[0])]
    elementary = sorted(elementary[1:], key = lambda x: x[0])

    new_one[0][7] = "ConfW";new_one[0][8] = "ConfL"
    new_one[0][9] = "HomeW";new_one[0][10] = "HomeL"
    new_one[0][11] = "AwayW";new_one[0][12] = "AwayL"
    
    new_one[0] = ['School', 'G', 'W', 'L', 'W-L%', 'SRS', 'SOS', 'ConfW', 'ConfL', 'HomeW', 'HomeL', 'AwayW', 'AwayL', 'Tm.', 'Opp.','MP', 'FG', 'FGA', 'FG%', '3P', '3PA', '3P%', 'FT', 'FTA', 'FT%', 'ORB', 'TRB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'Pace', 'ORtg', 'FTr', '3PAr', 'TS%', 'TRB%', 'AST%', 'STL%', 'BLK%', 'eFG%', 'TOV%', 'ORB%', 'FT/FGA', 'AdjEM', 'AdjO', 'AdjD', 'AdjT', 'Luck', 'SOS AdjEM', 'OppO', 'OppD', 'NCSOS AdjEM']
    
    index = 0
    for i in reader[1:]:
        while elementary[index][0] != i[0]:
            index+=1
        new_one.append(formula(i, elementary[index]))

    with open("ncaa" + str(year) + ".csv", "w",newline = "") as page:
        spamwriter = csv.writer(page, delimiter = ',')
        for i in new_one:
            spamwriter.writerow(i)

    print("Done")

    
