import requests
from bs4 import BeautifulSoup
import csv



#Returns table heading
def heading(file):
    name_box = file.find('thead').find_all('tr')
    return [i.contents[0]  for i in name_box[1].find_all('th') if i.contents[0] != '\xa0' ][1:]


#Returns school name, returns None if invalid row
def get_school(row):
    k = row.find('td',attrs= {'class':'left '})
    if k == None:
        return None
    return k.find('a').contents[0]

#Returns the row of data
#Precondition: Valid row
def get_fields(row):
    k = row.find_all("td",attrs = {'class':'right'})
    return [get_school(row)] + [i.contents[0] for i in k if len(i.contents) != 0 ]


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

