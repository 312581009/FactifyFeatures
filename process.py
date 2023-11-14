inFile = 'data.json'
outFile = 'process.json'

import json
f = open(inFile)
input = json.load(f)

output = []
import os.path
if os.path.isfile(outFile):
    f2 = open(outFile)
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
    addFeature(output[i])

from itertools import product
keys = data.keys()
features = [item for item in keys if item not in ['id', 'claim_id', 'claim', 'evidence', 'question', 'claim_answer', 'evidence_answer', 'label']]
#['characters', 'words', 'capital_characters', 'capital_words', 'punctuations', 'quotes', 'sentences', 'uniques', 'hashtags', 'mentions', 'stopwords']

#single features
for i in range(5):
    for f in features:
        temp = [d[f][i] for d in input]
        num = max(temp)
        norm = [float(id)/num if num != 0 else 0 for id in temp]
        for index in range(len(input)):
            output[index]['feature'].append((norm[index] * 2) - 1.0)

#combination features
for i in list(product([0, 1, 2, 3, 4], repeat=2)):
    for f in list(product(features, repeat=2)):
        f1 = [d[f[0]][i[0]] for d in input]
        f2 = [d[f[1]][i[1]] for d in input]
        if f1 == f2:
            continue
        result = []
        for id in range(len(f1)):
            if f2[id] != 0:
                result.append(f1[id] / f2[id])
            else:
                result.append(0)
        num = max(result)
        norm = [float(id)/num if num != 0 else 0 for id in result]
        for index in range(len(input)):
            output[index]['feature'].append((norm[index] * 2) - 1.0)

with open(outFile, 'w') as f:
    json.dump(output, f)