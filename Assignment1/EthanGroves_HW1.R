# Aug 30, 2014
# Ethan Groves
# CMDA 3654
# Homework 1

##################################################################
#                                                                #
#                           PROBLEM 1                            #
#                                                                #
##################################################################

getwd()
setwd("/Users/ethangroves/Desktop/Fall 2014/CMDA 3654/CMDA/Assignment1")

# Import prices data-sheet
# Create variable names for the data-frame within the
# read.table function (Use col.names argument)
pricesData <- read.table(
  'prices.csv',
  sep=',',
  header=T,
  col.names = c("Prices","SqFt","Age","NE")
)

# Print data-frame
print(pricesData)

# Find out what row.names argument does (for function read.table).
# Describe in one line comment.
# row.names is used to create row names

##################################################################
#                                                                #
#                           PROBLEM 2                            #
#                                                                #
##################################################################

# Create a 4 X 4 matrix MAT1 using the cbind(function).
c1 = c(1, 0, 0, 5)
c2 = c(0, 2, 6, 0)
c3 = c(0, 7, 3, 0)
c4 = c(8, 0, 0, 4)
MAT1 = cbind(c1, c2, c3, c4)

# How do you list the last element of the matrix with a one line command?
MAT1[4,4]

# Find the transpose of your matrix.
t(MAT1)

# Find the inverse of your matrix.
solve(MAT1)

##################################################################
#                                                                #
#                           PROBLEM 3                            #
#                                                                #
##################################################################

# Use dataset:
# fpe <- read.table("http://data.princeton.edu/wws509/datasets/effort.dat")
fpe <- read.table("http://data.princeton.edu/wws509/datasets/effort.dat")

# For the fpe dataset, print out only the observations with 0 effort.
nvariables <- dim(fpe)[1]
for(i in 1:nvariables) {
  if(fpe$effort[i] == 0) { # if variable i is effort level 0
    print(fpe[i,]) # Print row
    i
  }
}

# For the fpe dataset print the names of the variables using one function.
names(fpe)

# For the fpe dataset print the names of the rows using one function.
row.names(fpe)

# Find out what the head() function does and print out the result for the fpe data frame.
head(fpe)

# Export your fpe data frame as both a text and a csv file.
write.csv(fpe, file="mydatacsv1.csv")
write.table(fpe, file="mydatacsv1.txt", sep="\t")