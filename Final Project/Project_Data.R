# Project Data
# Stock Sentiment
# Team 4

setwd("/Users/ethangroves/Desktop/Fall 2014/CMDA 3654/Data/")

stockData <- read.table('sp500hst.txt', 
                         sep=',', 
                         col.names = c("Date","Stock","Open","High","Low","Close","Volume"))

twitterData <- read.table('training.1600000.processed.noemoticon.csv',
                          sep=',',
                          col.names = c("Polarity","ID","Date","Query","User","Tweet"))