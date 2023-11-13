import json
f = open('data.json')
input = json.load(f)

output = []
import os.path
if os.path.isfile('process.json'):
    f2 = open('process.json')
    output = json.load(f2)
else:
    output = [{} for _ in range(len(input))]

claim = evidence = ''
question = claim_answer = evidence_answer = []

def getFeature(func):
    return [func(claim), func(evidence), 
            sum(func(q) if q else 0 for q in question), 
            sum(func(c) if c else 0 for c in claim_answer), 
            sum(func(e) if e else 0 for e in evidence_answer)]

import string
import re
import nltk
nltk.download('punkt')
nltk.download('stopwords')
stopwords = set(nltk.corpus.stopwords.words("english"))
def addFeature(instance):
    # EXISTING DATA DOES NOT NEED TO BE RUN AGAIN
    instance['id'] = id
    instance['claim_id'] = claim_id
    instance['claim'] = claim
    instance['evidence'] = evidence
    instance['question'] = question
    instance['claim_answer'] = claim_answer
    instance['evidence_answer'] = evidence_answer
    instance['label'] = label
    instance['feature'] = []
    return

    # https://www.analyticsvidhya.com/blog/2021/04/a-guide-to-feature-engineering-in-nlp/
    # ADDITIONAL CALCULATIONS
    # avg_word_len = characters/words
    # avg_sentence_len = words/sentences
    # unique_ratio = uniques/words
    # stopword_ratio = stopwords/words

def removeFeature(instance):
    # ADD STRING NAME OF FEATURE TO REMOVE
    remove = []
    for feature in remove:
        instance.pop(feature, None)

for i, data in enumerate(input):
    batch_size = 100
    if i % batch_size == 0:
        print(f"Processing batch {int(i / batch_size) + 1} of {int(len(input) / batch_size)}")

    id = data['id']
    claim_id = data['claim_id']
    claim = data['claim']
    evidence = data['evidence']
    question = data['question']
    claim_answer = data['claim_answer']
    evidence_answer = data['evidence_answer']
    label = data['label']

    removeFeature(output[i])
    addFeature(output[i])

from itertools import product
features = ['characters', 'words', 'capital_characters', 'capital_words', 'punctuations', 'quotes', 'sentences', 'uniques', 'hashtags', 'mentions', 'stopwords']

#single features
for i in range(5):
    for f in features:
        temp = [d[f][i] for d in input]
        num = max(temp)
        norm = [float(id)/num if num != 0 else 0 for id in temp]
        for index in range(len(input)):
            output[index]['feature'].append((norm[index] * 2) - 1.0)

#combination features
for porder in list(product([0, 1, 2, 3, 4], repeat=2)):
    for p in list(product(features, repeat=2)):
        temp2 = [d[p[0]][porder[0]] for d in input]
        temp3 = [d[p[1]][porder[1]] for d in input]
        if temp2 == temp3:
            continue
        temp = []
        for id in range(len(temp2)):
            if temp3[id] != 0:
                temp.append(temp2[id] / temp3[id])
            else:
                temp.append(0)
        num = max(temp)
        norm = [float(id)/num if num != 0 else 0 for id in temp]
        for index in range(len(input)):
            output[index]['feature'].append((norm[index] * 2) - 1.0)

with open('process.json', 'w') as f:
    json.dump(output, f)