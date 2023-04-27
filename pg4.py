import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
 
sentences=["This is a good job.I will not miss it for anything",
           "This is not good at all"]
 
cv = CountVectorizer(ngram_range=(1,1), stop_words='english')
 
cv_matrix = cv.fit_transform(sentences)
 
cv_dataframe=pd.DataFrame(cv_matrix.toarray(),columns=cv.get_feature_names_out())
print(cv_dataframe)
