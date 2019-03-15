import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression as line, LogisticRegression as logit
from math import log
from itertools import compress
import csv

def download(years, params):
    X = []
    Y = []
    for year in years:
        with open('ncaa' + str(year) + 'gamesdata.csv') as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            parameters = [int(i in params) for i in range(111)]
            for n,i in enumerate(readCSV):
                if n != 0:
                    X.append(list(compress(i, parameters)))
                    X[-1] = [float(i) for i in X[-1]]
                    Y.append(int(i[4]))
    return X,Y

def log_loss(true, pred, cap = pow(10, -5)):
    pred = max(min(pred, 1 - cap), cap)
    return true * log(pred) + (1-true) * log(1-pred)

heading = ['Team1', 'Team2', 'Points1', 'Points2', 'Result', 'G1', 'W1', 'L1', 'W-L%1', 'SRS1', 'SOS1', 'ConfW1', 'ConfL1', 'HomeW1', 'HomeL1', 'AwayW1', 'AwayL1', 'Tm.1', 'Opp.1', 'MP1', 'FG1', 'FGA1', 'FG%1', '3P1', '3PA1', '3P%1', 'FT1', 'FTA1', 'FT%1', 'ORB1', 'TRB1', 'AST1', 'STL1', 'BLK1', 'TOV1', 'PF1', 'Pace1', 'ORtg1', 'FTr1', '3PAr1', 'TS%1', 'TRB%1', 'AST%1', 'STL%1', 'BLK%1', 'eFG%1', 'TOV%1', 'ORB%1', 'FT/FGA1', 'AdjEM1', 'AdjO1', 'AdjD1', 'AdjT1', 'Luck1', 'SOS AdjEM1', 'OppO1', 'OppD1', 'NCSOS AdjEM1', 'G2', 'W2', 'L2', 'W-L%2', 'SRS2', 'SOS2', 'ConfW2', 'ConfL2', 'HomeW2', 'HomeL2', 'AwayW2', 'AwayL2', 'Tm.2', 'Opp.2', 'MP2', 'FG2', 'FGA2', 'FG%2', '3P2', '3PA2', '3P%2', 'FT2', 'FTA2', 'FT%2', 'ORB2', 'TRB2', 'AST2', 'STL2', 'BLK2', 'TOV2', 'PF2', 'Pace2', 'ORtg2', 'FTr2', '3PAr2', 'TS%2', 'TRB%2', 'AST%2', 'STL%2', 'BLK%2', 'eFG%2', 'TOV%2', 'ORB%2', 'FT/FGA2', 'AdjEM2', 'AdjO2', 'AdjD2', 'AdjT2', 'Luck2', 'SOS AdjEM2', 'OppO2', 'OppD2', 'NCSOS AdjEM2']


'''How to use model():
train = training years as a list (e.g. [2015, 2016, 2017])
test_year = year we test on (integer)
params = columns we want to use (e.g. [28, 50, 51, 81 103, 104]) PRO TIP: Team 2 data is 53 after team 1 data
cap = how much we cap it on either end (the smallest percent chance is 10^(-5) right now), capping at 0.1 works

RETURNS:
the list of probabilities
prints the log loss
'''
def model(train, test_year, params, cap = pow(10, -5)):
    param = set(params)
    x,y = download(train, params)
    log = logit(solver = 'liblinear', max_iter = 1000).fit(np.array(x),np.array(y))

    test_x, test_y = download([test_year], params)
    array = [[test_y[i], log.predict_proba([test_x[i]])[0][1]] for i in range(len(test_x))]
    logs = [log_loss(i[0], i[1], cap) for i in array]
    print(-sum(logs)/len(logs))
    return array
   # return -1 * sum([log_loss(test_y[i], log.predict([test_x[i]])[0]) for i in range(len(test_x))])/len(test_x)

#2014 model: 6th place
print(2014)
z = model([2012, 2013, 2011], 2014, set({50,51,103, 104, 28, 81}), 0.05)

#2015 model: 6th place (0.454)
print(2015)
z = model([2012, 2013, 2014], 2015, set({50,51,103, 104, 28, 81}), 0.05)

#2016 model: 2nd place (0.495)
print(2016)
z = model([2013, 2015, 2014], 2016, set({50,51,103, 104, 28, 81}), 0.05)

#2017 model: 4th place (0.456)
print(2017)
z = model([2016, 2015, 2014], 2017, set({50,51,103, 104, 28, 81}), 0.05)

#2018 model: 2nd place (0.53196)
print(2018)
z = model([2016, 2015, 2017], 2018, set({50,51,103, 104, 28, 81}), 0.1)




'''Example how to use sklearn to do this:'''

def demonstrateLinReg():
    X = np.array([[0,0],[1,1],[2,2]])
    reg = line().fit(X, [0,1,2])
    #this does z = 0.5x + 0.5y , fitting to the points (0,0,0), (1,1,1), (2,2,2)

    print(reg.predict([[1,2]])) #(1,2,z) -> (1,2,1.5)
def demonstrateLogit():
    X = np.array([[0,0],[1,1],[2,2]])
    Y = [0,1,0]
    log = logit().fit(X,Y)

    return -1 * sum([log_loss(Y, log.predict([i])[0]) for i in X])/len(X)

