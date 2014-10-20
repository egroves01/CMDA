# Ethan Groves
# In Class 7
# 10/20/14

'''
############################################################################################
##                                  In Class 7.1                                          ##
############################################################################################
'''

# 1) Create a new ipython notebook.
import pandas as pd

# 2) Use the data for your project as a panda dataframe.
sp = pd.read_table('../Data/sp500hst.txt', sep = ',', names = ['Date','Symbol','Open','High','Low','Close','Volume'])
df = sp['High'].head(100)
df2 = sp['Low'].head(100)
sp

# 3) For suitable variables, plot :
#    1. a histogram;
df.hist(bins = 6)
#    2. a density plot;
df.plot(kind = 'kde')
#    3. a bar chart;
df.plot(kind = 'bar')
#    4. a horizontal stacked bar chart with categories summing to 1;
df_rel = df.div(sp.sum(1).astype(float),axis = 0)
df_rel.plot(kind = 'bar', stacked = True)
#    5. a scatterplot.
plt.scatter(df, df2)
plt.title("High vs. Low")

# 4) Save all figures as png in your working directory. Submit the pngs with your in class assignment.
# √

'''
############################################################################################
##                                  In Class 7.2                                          ##
############################################################################################
'''

# 1. Create a new ipython notebook Inclass7_2.ipynb.
import scipy as sp
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn as sk

# 2. Download Medical.csv from scholar/Data and import it as a pandas dataframe.
#    You will train a linear classifier to separate diabetic subjects 
#    (all subjects included in the dataset are diabetic) into two classes of health literacy 
#    (how much they know about health) based on their age and measured average blood glucose.
med = pd.read_table('../Data/Medical.csv', sep = ',')

# 3. Wrangle your data with pandas. Keep features “age” and “HgA1c”. Create target variable
#    literacy with levels 0=“low literacy” and 1= “high literacy” based on the dataframe’s 
#    variable “literacy” with levels “low” and “high”.
mapping = {'LOW': 0, 'HIGH': 1}
newMap = med['A Literacy Category'].map(mapping)

# 4. Setup the numpy arrays X and y.
X = array(med[['Age', 'HgA1C']])
y = array(newMap)

# 5. Take a 75% training set and a 25% testing set using the scikit-learn capabilities.
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 33)
y_train  # Map high = 1; low = 0;

# 6. Scale your features.
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler().fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

# 7. Train the classifier. Write out the classifier’s equation.
'''
colors = ['red', 'greenyellow']
for i in xrange(len(colors)):
    px = X_train[:, 0][y_train == i]
    py = X_train[:, 1][y_train == i]
    plt.scatterplot(px, py, c = colors[i])
'''
from sklearn.linear_model import SGDClassifier
clf = SGDClassifier()
clf.fit(X_train, y_train)

# 8. What is the classifier’s accuracy on the training data?
from sklearn import metrics
y_train_pred = clf.predict(X_train)
metrics.accuracy_score(y_train, y_train_pred)

# 9. What is the classifier’s accuracy on the test set?
y_pred = clf.predict(X_test)
print metrics.accuracy_score(y_test, y_pred)

# 10. What is the confusion matrix and what is the interpretation of each number in the matrix?
metrics.confusion_matrix(y_test, y_pred)

# 11. Comment on the quality of this classifier for this problem.
#     Note: the ipython notebook with code, results and comments will be submitted as well
#     by the deadline of Inclass 7, to Dropbox and GitHub.