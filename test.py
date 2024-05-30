import requests

API_URL = "https://api-inference.huggingface.co/models/distilbert/distilbert-base-uncased-finetuned-sst-2-english"


with open('.hf_token', 'r') as file:
	token = file.read()

headers = {"Authorization": f"Bearer {token}"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
	
output = query({
		"inputs": "I don't like you. I hate you",
})

print(output)
