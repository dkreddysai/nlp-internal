import pandas as pd
from sklearn.feature_extraction.text import *
from sklearn.feature_extraction.text import CountVectorizer
text=["I Love writing code in python.I Love python code",
      "I hate writing code in java.I hate java code"]
df = pd.DataFrame({'review': ['review1', 'review2'], 'text':text})
cv = CountVectorizer(stop_words='english')
cv_matrix = cv.fit_transform(df['text'])
df_dtm=pd.DataFrame(cv_matrix.toarray(),index=df['review'],columns=cv.get_feature_names_out())
print(df_dtm)

