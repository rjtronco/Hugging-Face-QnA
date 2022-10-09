import requests
import json



def get_qa(topic, data):
    q = []
    a = []
    for d in data['data']:
        if d['title']==topic:
            for paragraph in d['paragraphs']:
                for qa in paragraph['qas']:
                    if not qa['is_impossible']:
                        q.append(qa['question'])
                        a.append(qa['answers'][0]['text'])
            return q,a

with open('train-v2.0.json') as json_file:
    json_data = json.load(json_file)
 
questions, answers = get_qa(topic='Premier_League', data=json_data  )

json_data = {
  'questions':questions,
  'answers':answers,
}

response = requests.post(
  'http://13.229.63.24/set_context',
  json=json_data
)

print(response.json())
