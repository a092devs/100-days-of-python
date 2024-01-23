import requests
from question_model import Question

URL = "https://opentdb.com/api.php"


def quiz_data(amount, category, difficulty):
    parameters = {
        "amount": int(amount),
        "category": category,
        "difficulty": difficulty.lower(),
        "type": "boolean",
    }

    if category == 0:
        del parameters["category"]
    if difficulty.lower() == "any difficulty":
        del parameters["difficulty"]
    question_response = requests.get(URL, params=parameters)
    question_response.raise_for_status()
    temp = question_response.json()
    question_data = temp["results"]
    return [Question(q["question"], q["correct_answer"]) for q in question_data]
