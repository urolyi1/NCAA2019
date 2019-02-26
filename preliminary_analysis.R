library(readr)

ncaa2012 <- read_csv("~/repositories/NCAA2019/statsandgames/ncaa2012gamesdata.csv")
score1 = ncaa2012$Points1
ncaa2012$SOS
score2 = ncaa2012$Points2

y <- lm((Points1 - Points2) ~ AdjEM1 + AdjEM2, data=ncaa2012)
summary(y)
