# Ethan Groves
# In Class 6
# 10/13/14

'''
############################################################################################
##                                  In Class 6.1                                          ##
############################################################################################
'''

# 1) Download data from Scholar/Resources/Data/Ch06.
# √

# 2) Create a new ipython notebook, Inclass6_1.
# √

# 3) Import work_tab, work_comma, and last two observations from 
#    stress2_1 file as pandas DataFrames. If needed, manage data to 
#    display in correct format as a pandas Data Frame.

import pandas as pd
import requests
import json

wt = pd.read_table('../Data/InClass6/work_tab.txt')
wc = pd.read_table('../Data/InClass6/work_comma.csv')

# 4) Use the github API to create a pandas data frame with 4 columns from the returned results.
r = requests.get('https://api.github.com/events')

t = r.json()
fields = ['created_at', 'public', 'type', 'test']
data_fr = pd.DataFrame(t, columns = fields)

# 5) Save the DF from part 4 as a pickle. Load the pickle.
data_fr.to_pickle('dframe_pickle')
pd.read_pickle('dframe_pickle')

# 6) Save the data in part 4 in HDF5 format. Access it.
store = pd.HDFStore('mydata.h5')
store['obj1'] = data_fr
store['obj1']

'''
############################################################################################
##                                  In Class 6.2                                          ##
############################################################################################
'''


import pandas as pd

# 1) Import your project data using one of the read_csv or read_table methods for pandas.
sp = pd.read_table('../Data/sp500hst.txt', sep = ',', names = ['Date','Symbol','Open','High','Low','Close','Volume'])
tw = pd.read_table('../Data/training.1600000.processed.noemoticon.csv', sep = ',', names = ['Polarity','ID','Date','Query','User','Tweet'])


# 2) Describe your dataframe using.describe() method.
tw.describe()
sp.describe()

# 3) Choose one numeric variable and transform it into categorical, with 3-5 categories.
bins = [0,20,40,60,80,100,120,160,200,300,500]
categorical = pd.cut(sp['High'], bins)

# 4) Get the frequencies for the categorical variable created in part 3.
pd.value_counts(categorical)

# 5) Create an additional variable using mapping and using the categorical variable from part 3.
#    Your map dictionary should have two elements.

# 6) Rename two columns in your data using .rename.

# 7) Extract a 50% training set using cut random permutations of rows 
#    (eg. If you have 101 rows in your dataframe, a 50% training set will have about 51 rows).

# 8) Extract a second 50% training set.

# 9) Combine the two training sets into a third dataframe.

# 10) Get rid of duplicate rows by using: dataframe_name.drop_duplicates().
#     What percentage of the rows do you have left?



