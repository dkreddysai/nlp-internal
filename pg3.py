import pandas as pd
from numpy import *
from sklearn.feature_extraction.text import CountVectorizer
sentences=["jim and pam travelled by the bus",
           "the train was late",
           "the flight was full.Travelling by flight is expansive"]
cv =CountVectorizer()
 
B_O_W = cv.fit_transform(sentences).toarray()
 
print("index in model")
print(cv.vocabulary_)
print("\n")
 
print("Features")
print(cv.get_feature_names_out())
print("\n")
 
print("BAG OF WORDS")
print(B_O_W)
