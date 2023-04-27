import nltk
from nltk import sent_tokenize
from nltk import word_tokenize
from nltk.probability import FreqDist
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
# open the text file
f = open("textfile.txt", encoding="utf8")
#read data
text=f.read()
print(text)
print("\n")
#data type of read data
print(type(text))
print("\n")
#length of the text
print(len(text))
#tokenize the text by sentence
sentences=sent_tokenize(text)
print(sentences)
#no of sentenses
print(len(sentences))
#tokenize the text by words
words=word_tokenize(text)
print(words)
#no of words
print(len(words))
#find the frequence of words
fdist=FreqDist(words)
#print(10 most common words)
com=fdist.most_common(10)
print(com)
#plot graph for10 most common words
fdist.plot(10)
#remove punctuation words
#empty list to store words
list=[]
#remove punctuation marks
for w in words:
    if w.isalpha():
        list.append(w.lower())
#print the words without punctuation marks
print(list)
print("\n")
#print no of words
print(len(list))
#plotting the graph without functuation marks
fdist=FreqDist(list)
fdist.plot(10)

#list of stopwords
st=stopwords.words("english")
print("\n")
print(st)
print(len(st))

#remove stopwords
#empty list to store words
list1=[]
#remove stopwords
for w in list:
    if w not in st:
        list1.append(w.lower())
#print the words without stopwords 
print(list1)
fdist=FreqDist(list1)
com=fdist.most_common(10)
print(com)
fdist.plot(10)
print("\n")


