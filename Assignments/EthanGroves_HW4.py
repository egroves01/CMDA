# Ethan Groves
# Team 4
# Homework 4
# Oct 20, 2014

# 1) Create a new ipython notebook.
import sklearn as sk
import numpy as np
import scipy as sp
import pandas as pd
import matplotlib.pyplot as plt

# 2) Discuss with your team and decide if you would like to use the same data set for your final
#    project. You can stay with it or you can find a new one. Data can come from a csv file, a text file,
#    or a JSON object.
'''
Our team decided to stay with our current data set.
'''

# 3) Import your data set to pandas. Re-create any reshaping operations you did in R for homework
stockData = pd.read_table('../Data/sp500hst.txt', sep = ',', names = ['Date','Symbol','Open','High','Low','Close','Volume'])


twitterData = pd.read_table('../Data/testdata.manual.2009.06.14.csv', # temporary subset of data for debugging
                          sep=',',
                          names = ['Polarity', 'ID', 'Date', 'Query', 'User', 'Tweet']);


# 4) Get numerical summaries for all your variables.
stockData.describe()
twitterData.describe()

# 5) Comment on and perform any needed treatment for missing values.
'''
There are no missing values.
'''

# 6) Comment on and perform any needed data transformations.
twitterData['Positive'] = np.where(twitterData['Polarity'] == 4, 'TRUE', 'FALSE');
twitterData['Negative'] = np.where(twitterData['Polarity'] == 0, 'TRUE', 'FALSE');

# 7) Get three visualizations that you consider meaningful.
twitterData['Polarity'].hist(bins = 3)
stockData['High'].plot(kind = 'kde')
plt.scatter(stockData['High'], stockData['Low'])

# 8) Save your data as a pickle.
twitterData.to_pickle('twitter_pickle')
stockData.to_pickle('stock_pickle')

# 9) Update your project repository on Git with the pickled file. Include a comment of what you did
#   in the description of the commit.
# √

# 10) Download your HW4 notebook as .py, and upload it to Dropbox and GitHub.
# √