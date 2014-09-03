#######################################################################
#                 Ethan Groves in class exercise
#######################################################################
# Get working directory
getwd()
#2 Set working directory
setwd("/Users/ethangroves/Desktop/Fall 2014/CMDA 3654/Data")
#3Import dataset
carsData<- read.table('cars1.csv', sep=',', header=T)
#4 Display the dimensions of the dataset
dim(carsData)
#5 What are the variable names in this data frame?
names(carsData)
#6 Assign the value of the cell [2,3] to a new variable var1
var1 <- carsData[2,2]
#7 Output the content of the first and second columns seperately
carsData[,1]
carsData[,2]
#8 Assign the values of variable "speed" from the data frame to a
# new variable "SPEED".  Print the new variable.
SPEED <- carsData$speed
print(SPEED)
# 9 Output the value of row 15 from the data frame
carsData[15,]
