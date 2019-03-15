library(readr)
library(Metrics)

file_path <- "~/repositories/NCAA2019/statsandgames/" #change to your file path to the data



files <- list.files(path=file_path, pattern="*.csv") #get all files with .csv extension

ncaaData <- read.csv(paste(file_path, files[1], sep=""), check.names=TRUE) #add first year

for (i in 2:length(files)) {
  temp <- read.csv(paste(file_path, files[i], sep=""), check.names=TRUE)
  ncaaData <- rbind(ncaaData, temp) #append next year
}

startYear <- 2014
endYear <- 2016
testYear <- 2017

startIndex <- (startYear - 2002) * 63 + 1
endIndex <- ((endYear + 1) - 2002) * 63 + 1
trainingData <- ncaaData[startIndex:endIndex,]

testStart <- (testYear - 2002) * 63 + 1
testEnd <- testStart + 62
testData <- ncaaData[testStart:testEnd,]

model <- glm(Result ~ AdjO1 + AdjO2 + AdjD1 + AdjD2 + FT.1 + FT.2, data=trainingData, family="binomial")

#create linear model to predict margin
points <- lm(Points1 - Points2 ~ AdjO1 + AdjO2 + AdjD1 + AdjD2 + FT.1 + FT.2, data=trainingData)
#predict margins for training data
pred_margin <- predict(points, trainingData, type="response")
model2 <- glm(Result ~ pred_margin, data=trainingData, family = "binomial")

#test data predicted margin
pred_margin2 <- predict(points, testData, type="response")
margin <- data.frame(pred_margin = pred_margin2)

#predicted outcome of games
pred <- predict(model, testData, type="response")
pred2 <- predict(model2, margin, type="response")

#capping
ind <- pred < .05
pred[ind] <- .05
ind <- pred > .95
pred[ind] <- .95

ind <- pred2 < .05
pred2[ind] <- .05
ind <- pred2 > .95
pred2[ind] <- .95


logLoss(testData$Result, pred)
logLoss(testData$Result, pred2)