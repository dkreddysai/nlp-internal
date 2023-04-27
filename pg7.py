import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.feature_extraction.text import CountVectorizer
cv=CountVectorizer()
data=pd.read_csv("train.csv")
data.head()
print(data.head(5))

