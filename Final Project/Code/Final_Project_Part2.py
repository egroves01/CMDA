
# coding: utf-8

# In[51]:

# Finish data wrangling and create graphs
# Stock Sentiment
# Ethan, Sarah, and Brandon

# Import libraries
import pandas as pd
from datetime import datetime
get_ipython().magic(u'matplotlib inline')
import matplotlib as mp
import matplotlib.pyplot as plt
import numpy as np


# In[52]:

# Import data
Stock_Polarity = pd.read_csv("Stock_Polarity_Data.csv") # Index, Symbol, Date, Close, Polarity
Twitter_Positivity = pd.read_csv("Twitter_Positivity_Data.csv")
Twitter_Positivity = Twitter_Positivity.drop(["Unnamed: 0"], axis=1)


# In[68]:

# Compress the stock data into compressed overall data
unique_dates = pd.unique(Stock_Polarity["Date"])
positives = {}
totals = {}
percent = {}
for date in unique_dates:
    positives[date] = Stock_Polarity[(Stock_Polarity["Date"] == date) & (Stock_Polarity["Polarity"] == 1)].count()["Polarity"]
    totals[date] = Stock_Polarity[(Stock_Polarity["Date"] == date)].count()["Polarity"]
    percent[date] = float(positives[date]) / float(totals[date])


# In[54]:

# Create new compressed data frame
df1 = pd.DataFrame(positives.items(), columns=["Date","PositiveStocks"])
df2 = pd.DataFrame(totals.items(), columns=["Date","TotalStocks"])
df3 = pd.DataFrame(percent.items(), columns=["Date","StocksPercentPositive"])

Stock_Data = df1.merge(df2).merge(df3, sort=True)


# In[55]:

Master_Data = Stock_Data.merge(Twitter_Positivity, sort=True, how="inner", on=["Date"])
Master_Data["DateInt64"] = pd.to_datetime(Master_Data.Date).astype(np.int64)


# In[71]:

Master_Data


# In[74]:

# Create a line graph of the data
line_graph = Master_Data.plot(kind="line", x="DateInt64", y=["Percentage","StocksPercentPositive"], title="Twitter Percentage of Positve Tweets to Percent of Increasing Stocks 6/1/09 to 6/5/09", legend=False)
patches, default_labels = line_graph.get_legend_handles_labels()
line_graph.legend(patches, ["Twitter Percentage Positive", "Stocks Percentage Positive"], loc="best")
line_graph.set_xlabel("Date as Int64 Representation")
line_graph.set_ylabel("Positive Percentage")
line_graph.set_xlim(1241136000000000000,1244160000000000000)


# In[75]:

# Save the graoh
line_graph.get_figure().savefig("linegraph.png")


# In[72]:




# In[ ]:



