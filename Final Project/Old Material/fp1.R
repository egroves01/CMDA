library(ggplot2)

'''
- Ensure all dates are of uniform format.
- Organize all data by date.
- Determine whether the cumulative stock trend for a given day was positive, negative, or neutral.
- Determine whether the cumulative twitter sentiment for a given day was positive, negative, or neutral.

Create two line graphs showing average stock prices over time and stacked bar graph showing the % tweets that are positive, negative, or neutral.

Predict whether stocks are going up or down for randomly chosen days and see how accurate the model is.

Perform Precision, Recall, Sensitivity, and/or Specificity tests on predictions (Using confusion matrix).
'''


setwd("/Users/ethangroves/Desktop/Fall 2014/CMDA 3654/Final_Project")

sp500 <- read.csv('sp500hst.txt', header = F, sep = ',')

# gives a logical vector telling you if A_Pval is smaller than 0.05
temp_A <- sp500$V2 == 'A'
company_A <- sp500[temp_A,]

# gives a logical vector telling you if B_Pval is smaller than 0.05
significant_B <- mydata$B_Pval<0.05

# gives a logical vector telling you if C_Pval is smaller than 0.05
significant_C <- mydata$C_Pval<0.05

# combine the results to one logical vector
# significant_all[i] has value TRUE if all the p-values in row i
# are smaller than 0.05

significant_all <- significant_A & significant_B & significant_C

# pick the rows you want
mydata[significant_all,]