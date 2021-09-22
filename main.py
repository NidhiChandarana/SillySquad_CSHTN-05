import nltk 
from nltk.stem.lancaster import LancasterStemmer
import numpy
import tensorflow
import tflearn
import random
import json

stemmer = LancasterStemmer()
with open("intents2.json") as file:
  data = json.load(file)
# print(data["intents"])

words = []
labels = []
docs_x = []
docs_y = []

for intent in data["intents"]:
  for pattern in intent["patterns"]:
    wrds = nltk.word_tokenize(pattern)
    words.extend(wrds)
    docs_x.append(pattern)
    docs_y.append(intent["tag"])

  if intent["tag"] not in labels:
    labels.append(intent["tag"])

words = [stemmer.stem(w.lower()) for w in words]
words = sorted(list(set(words)))

labels = sorted(labels)
training = []
output = []

out_empty = [0 for _ in range(len(labels))]

for x,doc in enumerate(docs_x):
  bag = []
  
  wrds = [stemmer.stem(w) for w in doc]

  for w in words:
    if w in wrds:
      bag.append(1)
    else:
      bag.append(0)

  output_row = out_empty[:]
  output_row[labels.index(docs_y[x])] = 1


  training.append(bag)
  output.append(output_row)

training = numpy.array(training)
output = numpy.array(output)
