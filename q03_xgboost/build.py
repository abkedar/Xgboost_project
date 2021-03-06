# %load q03_xgboost/build.py
# Default imports
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
import pandas as pd
from sklearn.metrics import accuracy_score

# load data
dataset = pd.read_csv('data/loan_clean_data.csv')
# split data into X and y
X = dataset.iloc[:, :-1]
y = dataset.iloc[:, -1]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=9)


# Write your solution here :
def xgboost(X_train, X_test, y_train, y_test, **kwargs):
    xgb = XGBClassifier(seed = 9)
    xgb.set_params(**kwargs)
    xgb.fit(X_train,y_train)
    return accuracy_score(y_test,xgb.predict(X_test))




