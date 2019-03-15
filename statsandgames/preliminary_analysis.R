library(readr)
ok <- read_csv("ncaa2016gamesdata.csv")
ok <- ok + read_csv("ncaa2017gamesdata.csv")
ok <- ok + read_csv("ncaa2015gamesdata.csv")
ok <- ok + read_csv("ncaa2014gamesdata.csv")
#ncaa2018 <- ncaa2018 +  read_csv("~/ncaa2017gamesdata.csv")
#ncaa2018 <- ncaa2018 +  read_csv("~/ncaa2016gamesdata.csv")
#ncaa2018 <- ncaa2018 +  read_csv("~/ncaa2015gamesdata.csv")
#ncaa2018 <- ncaa2018 +  read_csv("~/ncaa2014gamesdata.csv")
#model <- lm((ncaa2018$Points1 - ncaa2018$Points2) ~ (ncaa2018$`3P%1`* (ncaa2018$`3PA1`/ ncaa2018$G1)) + 
 #             (ncaa2018$`3P%2`* (ncaa2018$`3PA2`/ ncaa2018$G2)) + (ncaa2018$`FG%2`* (ncaa2018$`FGA2`/ ncaa2018$G2)) +
  #            (ncaa2018$`FG%2`* (ncaa2018$`FGA2`/ ncaa2018$G2)))
model <- lm((ok$Points1 - ok$Points2) ~ ok$AdjD1 + ok$AdjD2 + ok$AdjO1*ok$AdjT1
            + ok$AdjO2*ok$AdjT2 + ok$`FT%1`  + ok$`FT%2`)
summary(model)
print(summary(model))
