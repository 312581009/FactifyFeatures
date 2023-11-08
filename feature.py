import json
f = open('train.json')
input = json.load(f)

output = []
import os.path
if os.path.isfile('data.json'):
    f2 = open('data.json')
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
    #instance['id'] = id
    instance['claim_id'] = claim_id
    instance['claim'] = claim
    instance['evidence'] = evidence
    instance['question'] = question
    instance['claim_answer'] = claim_answer
    instance['evidence_answer'] = evidence_answer
    instance['label'] = label
    #instance['characters'] = getFeature(len)
    #instance['words'] = getFeature(lambda x: len(x.split()))
    #instance['capital_characters'] = getFeature(lambda x: len([char for char in x if char.isupper()]))
    #instance['capital_words'] = getFeature(lambda x: len([word for word in x.split() if any(char.isupper() for char in word)]))
    #instance['punctuations'] = getFeature(lambda x : sum(1 for char in x if char in string.punctuation))
    #instance['quotes'] = getFeature(lambda x : len(re.findall(r'"([^"]*)"', x)))
    #instance['sentences'] = getFeature(lambda x : len(nltk.sent_tokenize(x)))
    #instance['uniques'] = getFeature(lambda x : len(set(x.split())))
    #instance['hashtags'] = getFeature(lambda x : len(re.findall(r'#\w+', x)))
    #instance['mentions'] = getFeature(lambda x : len(re.findall(r'@\w+', x)))
    #instance['stopwords'] = getFeature(lambda x : len([word for word in x.split() if word.lower() in stopwords]))
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

with open('data.json', 'w') as f:
    json.dump(output, f)