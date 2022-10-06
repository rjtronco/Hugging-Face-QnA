import requests

json_data = {
  'questions':questions,
  'answers':answers,
}

response = requests.post(
  'http://0.0.0.0:8000/set_context',
  json=json_data
)

response.json()