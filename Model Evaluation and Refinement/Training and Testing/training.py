#splitting data for test and train
# and then checking how fit is our data
#R^2

import pandas as pd
import numpy as np
from IPython.display import display
from IPython.html import widgets 
from IPython.display import display
from ipywidgets import interact, interactive, fixed, interact_manual
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


path = 'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DA0101EN/module_5_auto.csv'
df = pd.read_csv(path)
df=df._get_numeric_data()
y_data = df['price']
x_data=df.drop('price',axis=1)
x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, test_size=0.15, random_state=0)


print("number of test samples :", x_test.shape[0])
print("number of training samples:",x_train.shape[0])
lre=LinearRegression()
lre.fit(x_train[['horsepower']], y_train)


a=lre.score(x_test[['horsepower']], y_test)
b=lre.score(x_train[['horsepower']], y_train)
print(a,b)
