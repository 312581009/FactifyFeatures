import openai
openai.api_key = open("key.txt", "r").read().strip("\n")

import json
f = open('train.json')
input = json.load(f)

output = []
import os.path
if os.path.isfile('data.json'):
    f2 = open('data.json')
    output = json.load(f2)
else:
    output = ["" for _ in range(len(input))]

for i in range(21, min(len(input), 25)):
  sp = r"System Prompt: given claim text and evidence text, determine the probabilities that the evidence refutes, supports and is neutral against the claim. Finish with either the {Support} {Refute} or {Neutral} label on the last line."
  message = sp + " Claim: " + input[i]['claim'] + " Evidence: " + input[i]['evidence']
  completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages = [{"role": "user", "content": message[:16384]}]
  )

  respond = completion.choices[0].message.content[-100:]
  front = respond.find('{')
  end = respond.find('}')
  if (front != -1 and end != -1):
    result = respond[front + 1:end]
    output[i] = result
    with open('data.json', 'w') as f:
      json.dump(output, f)
    print(i, ": ", result)
  else:
     print(i, ": Not Found")