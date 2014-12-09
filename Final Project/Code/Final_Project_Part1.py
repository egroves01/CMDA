
# coding: utf-8

# In[32]:

# Data wrangling
# Stock sentiment
# Ethan, Sarah, and Brandon

# Import libraries
import pandas as pd
import pyper as pr
from datetime import datetime


# In[14]:

# Set the R directory then load PypeR
r_dir = "E:\\Program Files\\R\\R-3.0.3\\bin\\R"

r = pr.R(RCMD=r_dir, use_pandas=True)


# In[50]:

# Load the data into Pandas
stock_csv_data = pd.read_csv("newSP500.csv", names=["Symbol","Date","Open","High","Low","Close","Volume", "AdjustedClose"])
twitter_csv_data = pd.read_csv("training.1600000.processed.noemoticon.csv", names=["Polarity","ID","Date","Query","User","Tweet"])


# In[51]:

# Delete unnecessary columns
stock_csv_data = stock_csv_data.drop(["Open", "High", "Low", "Volume", "AdjustedClose"], axis=1)
twitter_csv_data = twitter_csv_data.drop(["ID", "Query", "User", "Tweet"], axis=1)


# In[53]:

# Convert stock dates to proper dates
stock_csv_data["Date"] = stock_csv_data["Date"].apply(lambda t: datetime.strptime(str(t), "%Y-%m-%d").date())


# In[54]:

# Convert twitter dates to proper datetimes
twitter_csv_data["Date"] = twitter_csv_data["Date"].apply(lambda t: datetime.strptime(t, "%a %b %d %H:%M:%S PDT %Y").date())


# In[58]:

# Makes tweet polarity equal to 1 or 0 rather than 4 or 0
twitter_csv_data["Polarity"] = twitter_csv_data["Polarity"].apply(lambda p: 1 if p == 4 else 0)


# In[108]:

# Create a new array that has all of the unique dates
unique_dates = pd.unique(twitter_csv_data["Date"])


# In[152]:

# Find the number of positive tweets for each unique date
# tdp = Total Daily Positives
tdp = {}
for date in unique_dates:
    ndfs = twitter_csv_data[(twitter_csv_data.Date == date) & (twitter_csv_data.Polarity == 1)].sum()
    tdp[date] = ndfs["Polarity"]


# In[151]:

# Find the total tweets in a day for each unique date
# ttd = Total Tweets Daily
ttd = {}
for date in unique_dates:
    ndfs = twitter_csv_data[(twitter_csv_data.Date == date)].count()
    ttd[date] = ndfs["Polarity"]


# In[153]:

# Find the percent of positive tweets over all tweets for each unique date
# ppd = Percent Positive Daily
ppd = {}
for date in unique_dates:
    ppd[date] = float(tdp[date]) / float(ttd[date])


# In[164]:

# Create dataframes for each of the dictionaries with the column names describing their values
df1 = pd.DataFrame(tdp.items(), columns=["Date", "Positives"])
df2 = pd.DataFrame(ttd.items(), columns=["Date", "Total"])
df3 = pd.DataFrame(ppd.items(), columns=["Date", "Percentage"])

# Create a new named dataframe that is a merging of df1, df2, and df3
Twitter_Positivity_Data = df1.merge(df2).merge(df3, sort=True)


# In[165]:

stock_csv_data.to_csv("simplified_stock.csv")
Twitter_Positivity_Data.to_csv("Twitter_Positivity_Data.csv")


# In[ ]:



