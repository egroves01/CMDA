#Lecture 7

getwd()
setwd("/Users/ethangroves/Desktop/Fall 2014/CMDA 3654/Data")

#The health insurance customer data
load('exampleData.rData')
#Examine data
names(custdata)
dim(custdata)
class(custdata)

#Summary statistics

summary(custdata) #for the entire data frame

#look at individual variables to spot problems

#########################################################################
# Comment on what you observe for each one of the variables in "custdata"
#########################################################################
summary(custdata$state.of.res)
# state.of.res: Shows how many residents per state.  There is data from all 50 states.
# There's a lot of people from California and New York.  Typical.

summary(custdata$custid)
# custid: Assuming the the customer id numbers were given incrementally from 1 to N,
# they have had over 1,400,000 customers.  Also, customer 2068 is probably old.

summary(custdata$sex)
# sex:  More males than females...

summary(custdata$is.employed)
# is.employed:  Lot's of NA's, which might actually represent unemployed people that were
# entered into the database incorrectly.

summary(custdata$income)
# income:  Minimum income is -8,700.  Either it's an error, or someone needs to get
# a new job.  I would like to make friends with the person making over $600K!

summary(custdata$marital.stat)
# marital.stat: Most people are married.  But some have died.  We dig deeper...
    nvariables <- dim(custdata)[1]
    widowed <- matrix(0,nrow=96,ncol= 1)
    counter <- 1
    for (i in 1:nvariables) {
      if (custdata$marital.stat[i] == "Widowed") {
        widowed[counter,1] <- paste(custdata$state.of.res[i])
        counter <- counter + 1
      }
    }
    summary(widowed)
# New York is not a good place to live happily ever after!  Stay away from New York.

summary(custdata$health.ins)
# health.ins:  Most people have health insurance.  Most people are paranoid.

summary(custdata$housing.type)
# housing.type: 157 customers are homeless and 11 live with their parents.
# Or maybe 157 own their homes...  That's probably a better guess.
# We also have 56 NA's.  Not good.

summary(custdata$recent.move)
# recent.move:  The majority of folks haven't moved recently.  Whatever recent means...
# We also have 56 NA's here as well.  That bodes ill for the data scientist.

summary(custdata$num.vehicles)
# num.vehicles:  Most people have two vehicles.  A pattern is emerging...  Another 56 NA's!

summary(custdata$age)
# age:  Ye olde Max is 146.7 years old!  It might be an entry mistake, or it might be a
# VAMPIRE!  Vampires live to be hundreds of years old.  Also, how can someone be zero
# years old?

summary(custdata$is.employed.fix1)
# is.employed.fix1: This summary is useless.  I can glean nothing of value. is.employed.fail

summary(custdata$age.normalized)
# age.normalized:  Not sure what I'm looking at here.  But it seems significant.

summary(custdata$Median.Income)
# Median.Income: The average income is $50K.  That seems like useful info.

summary(custdata$income.norm)
# income.norm:  These numbers seem to be very copacetic.  Resplendent.

summary(custdata$gp)
# gp: If I knew what gp stood for, I might have a chance at deciphering these numbers.

summary(custdata$income.lt.30K)
# income.lt.30K: Most people make over $30K.  But a significant percentage don't.
# Philosophy majors...

summary(custdata$age.range)
# age.range:  Most people are between the ages of 25-65.  There are 4 times as many customers
# over the age of 65 as there are under 25.

summary(custdata$Income)
# Income: Let's have income twice, just to confuse people.  This one is capitalized, for
# clarity.  Similar numbers, just way more NA's.  Note we didn't NA the $615K person.

#######################################################################
# Comment on what you observe for each one of the variables in "uciCar"
#######################################################################

uciCar <- read.table(
  'http://www.win-vector.com/dfiles/car.data.csv',
  sep=',',
  header=T
)

summary(uciCar$buying)
# buying: It would seem that there is not much variation...

summary(uciCar$maint)
# maint: Again, not much variation.

summary(uciCar$doors)
# doors: This information does not seem to be very helpful.

summary(uciCar$persons)
# persons: Not getting much out of this.

summary(uciCar$lug_boot)
# lug_boot: Still nothing useful.

summary(uciCar$safety)
# safety: How does this summary help anything?

summary(uciCar$rating)
# rating: Finally!  Something that actually means something.  Most ratings are unacceptable.

#############################################################################
# Comment on what you observe for each one of the variables in "credit.RData"
#############################################################################

load('credit.RData')

names(d)

summary(d$Personal.status.and.sex)
# Personal.status.and.sex: Not a very useful summary.

summary(d$Other.debtors/guarantors)
# Other.debtors/guarantors: Error in summary(d$Other.debtors/guarantors) : 
# object 'guarantors' not found
summary(as.factor(d[,10]))  # Equivalent to: d$Other.debtors/guarantors
# Length: 1000 Class/Mode: Character...  Not the most useful summary.