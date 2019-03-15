library(readr)
ncaa2018 <- read_csv("~/repositories/NCAA2019/statsandgames/ncaa2018gamesdata.csv")
ncaa2018 <- ncaa2018 +  read_csv("~/NCAA2019/statsandgames/ncaa2017gamesdata.csv")
ncaa2018 <- ncaa2018 +  read_csv("~/NCAA2019/statsandgames/ncaa2016gamesdata.csv")
ncaa2018 <- ncaa2018 +  read_csv("~/NCAA2019/statsandgames/ncaa2015gamesdata.csv")
ncaa2018 <- ncaa2018 +  read_csv("~/NCAA2019/statsandgames/ncaa2014gamesdata.csv")
#model <- lm((ncaa2018$Points1 - ncaa2018$Points2) ~ (ncaa2018$`3P%1`* (ncaa2018$`3PA1`/ ncaa2018$G1)) + 
 #             (ncaa2018$`3P%2`* (ncaa2018$`3PA2`/ ncaa2018$G2)) + (ncaa2018$`FG%2`* (ncaa2018$`FGA2`/ ncaa2018$G2)) +
  #            (ncaa2018$`FG%2`* (ncaa2018$`FGA2`/ ncaa2018$G2)))
model <- lm((ncaa2018$Points1 - ncaa2018$Points2) ~ ncaa2018$AdjD1 + ncaa2018$AdjD2 + ncaa2018$AdjO1*ncaa2018$AdjT1
            + ncaa2018$AdjO2*ncaa2018$AdjT2 + ncaa2018$`FT%1`  + ncaa2018$`FT%2`)
summary(model)