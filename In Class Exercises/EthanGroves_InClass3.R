getwd()
setwd("/Users/ethangroves/Desktop/Fall 2014/CMDA 3654/Data")

#reload the insurance data (new version of the file)

load("exampleData1.rData")

temp <- merge(medianincome, custdata)
summary(temp)

custdata$norm.income <- custdata$income/temp$Median.Income
summary(custdata$norm.income)

# Normalizing the income is useful, because the cost of living and the correlated income
# for a given area are different.  A good wage in Iowa could easily be a terrible wage
# in California since the average incomes for each state are different.

#30% of gp values are below 0.30 and 70% of the values are above 0.30.
#So split dataset according to values of gp. (percentages will be approximate)
testSet <- subset(custdata, custdata$gp <= 0.3)
trainingSet <- subset(custdata, custdata$gp > 0.3)