import requests

endpoint = "https://api.assemblyai.com/v2/transcript"

json = {
  "audio_url": "https://storage.googleapis.com/bucket/b2c31290d9d8.wav"
}

headers = {
  "Authorization": "10103d1330a1429eb01e826aa6fb59e6",
  "Content-Type": "application/json"
}

response = requests.post(endpoint, json=json, headers=headers)
print(response.json())