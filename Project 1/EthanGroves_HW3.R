# Ethan Groves
# Team 4
# Homework 3
# Sep 22, 2014

library("ggplot2");

# Part 1 - Load data
stockData <- read.table('sp500hst.txt',
                        sep=',',
                        col.names = c("Date", "Stock", "Open", "High", "Low", "Close", "Volume"));


twitterData <- read.table('testdata.manual.2009.06.14.csv', # temporary subset of data for debugging
                          sep=',',
                          col.names = c("Polarity", "ID", "Date", "Query", "User", "Tweet"));

# Part 2 - Numeric vs Factors
# After some discussion, it has been agreed that the "Polarity" variable would better
# server this study as a factor (boolean) rather than a numeric value.  It was also 
# noted that the "Open" variable could also be converted from a numeric value to a
# factor indicating whether the stock price went up or down compared to the "Close" variable
# over the course of a day of trading.

# Part 3
summary(stockData$Open)
summary(stockData$Date)
summary(stockData$Volume)
summary(twitterData$Positive)
summary(twitterData$Negative)
summary(twitterData$Date)

# Part 4
# TODO need to learn how to convert dates to a useful format
ggplot(data=subset(stockData, Stock == "AAPL"), aes(x=Date, y=Open)) + geom_line() + theme_bw() + ggtitle("Apple Stock Values Over Time")
ggplot(data=twitterData, aes(x=Positive)) + geom_bar() + theme_bw() + ggtitle("Positive Polarity Against Negative Polarity")
ggplot(data=subset(twitterData, Query == "kindle2"), aes(x=Positive)) + geom_bar() + theme_bw() + ggtitle("Positive Polarity Against Negative Polarity for the Kindle 2")

# Part 5
# No missing values in the data

# Part 6
# Create a factor denoting if the obs is positive or negative
twitterData$Positive <- ifelse(twitterData$Polarity == 4, TRUE, FALSE);
twitterData$Negative <- ifelse(twitterData$Polarity == 0, TRUE, FALSE);

# It was observed that in order for the "Date" variable to be useful, the data needs
# to be interpreted as a date.  Unfortunately, we have not learned how to do this conversion
# yet, but we are planning to pursue a solution to this issue.

# Part 7
save(stockData, twitterData, file="TransformedData.RData")

