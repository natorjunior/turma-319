# -*- coding: utf-8 -*-
"""Projeto 1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1svGXiDQsYVzhLICTo20O7dEMMossX65-
"""

import pandas as pd
import unicodedata
import re

df= pd.read_csv('https://raw.githubusercontent.com/natorjunior/debates-ideologicos/main/dataset.csv')
df.head()

import nltk
nltk.download('stopwords')
nltk.download('punkt')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
stop_words = set(stopwords.words('portuguese'))

stop_words

stop_words.remove('não')

stop_words

def preprocessing(text):
  word_tokens = word_tokenize(text)
  filtered_sentence = [w for w in word_tokens if not w.lower() in stop_words]
  filtered_sentence = []
  for w in word_tokens:
      if w not in stop_words:
          filtered_sentence.append(w)
  return " ".join(filtered_sentence)

df["tratadas"] = df.Text.apply(preprocessing)

df

from sklearn.feature_extraction.text import CountVectorizer
docs = df.tratadas

vectorizer = CountVectorizer()
bow_matrix = vectorizer.fit_transform(docs)

print(vectorizer.vocabulary_)

print(bow_matrix.toarray().shape)

from sklearn.model_selection import train_test_split
X_treino, X_teste, y_treino, y_teste = train_test_split(bow_matrix.toarray(), df.Label,
test_size=0.3,random_state=42)

from sklearn.naive_bayes import GaussianNB

clf = GaussianNB()
clf.fit(X_treino, y_treino)

from sklearn.metrics import confusion_matrix
y_true = y_teste
y_pred = clf.predict(X_teste)
confusion_matrix(y_true, y_pred)

from sklearn.metrics import accuracy_score
y_pred = clf.predict(X_teste)
y_true = y_teste
accuracy_score(y_true, y_pred)

from sklearn.metrics import precision_score
precision_score(y_true, y_pred)

from sklearn.metrics import recall_score
recall_score(y_true, y_pred)

from sklearn.metrics import f1_score
f1_score(y_true, y_pred)