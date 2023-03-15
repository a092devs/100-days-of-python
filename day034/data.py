import requests

paramaters = {
    "amount" : 10,
    "type" : "boolean"
}

resp = requests.get("https://opentdb.com/api.php", paramaters)
resp.raise_for_status()
data = resp.json()
question_data = data["results"]