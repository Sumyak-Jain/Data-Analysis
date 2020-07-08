# We will now predict car price with multiple variables like horsepower,compression_ratio etc

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
url = 'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DA0101EN/automobileEDA.csv'
df = pd.read_csv(url)
lm= LinearRegression()
lm
X = df[['horsepower','compression-ratio','city-mpg','highway-mpg']]
Y = df['price']
lm.fit(X,Y)
Yhat=lm.predict(X)
Yhat[0:5]
a=lm.intercept_
b=lm.coef_
# Yhat=a+b0X0+b1X1+b2X2+b3X3
print(a+b[0]*154+b[1]*9+b[2]*19+b[3]*26)
