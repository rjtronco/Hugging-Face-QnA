import requests

new_questions = [
    'How many teams compete in the Premier League ?',
    'When does the Premier League starts and finishes ?',
    'Who has the highest number of goals in the Premier League ?',
]

json_data = {
  'questions':new_questions,
}

response = requests.post(
  'http://0.0.0.0:8000/get_answer',
  json=json_data
)

for d in response.json():
  print('\n'.join(["{} : {}".format(k, v) for k,v in d.items()])+'\n')