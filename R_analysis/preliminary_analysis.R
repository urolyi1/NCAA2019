library(readr)
library(Metrics)

file_path <- "~/repositories/NCAA2019/statsandgames/" #change to your file path to the data



files <- list.files(path=file_path, pattern="*.csv") #get all files with .csv extension

ncaaData <- read.csv(paste(file_path, files[1], sep=""), check.names=TRUE) #add first year

for (i in 2:length(files)) {
  temp <- read.csv(paste(file_path, files[i], sep=""), check.names=TRUE)
  ncaaData <- rbind(ncaaData, temp) #append next year
}

startYear <- 2011
endYear <- 2014
testYear <- 2015

startIndex <- (startYear - 2002) * 63 + 1
endIndex <- (endYear - 2002) * 63 + 1
trainingData <- ncaaData[startIndex:endIndex,]

testStart <- (testYear - 2002) * 63 + 1
testEnd <- testStart + 62
testData <- ncaaData[testStart:testEnd,]

model <- glm(Result ~ AdjO1 + AdjO2 + AdjD1 + AdjD2 + FT.1 + FT.2, data=trainingData, family="binomial")
pred <- predict(model, testData, type="response")
ind <- pred < .05
pred[ind] <- .05
ind <- pred > .95
pred[ind] <- .95


logLoss(testData$Result, pred)