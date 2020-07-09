#Residual Plot to visualize fit of a model

import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
url = 'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DA0101EN/automobileEDA.csv'
df = pd.read_csv(url)
width=8
height=5
plt.figure(figsize=(width, height))
sns.residplot(df['peak-rpm'], df['price'])
plt.show()
