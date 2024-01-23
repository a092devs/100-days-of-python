import requests
from os import environ
from datetime import datetime
from dotenv import load_dotenv

load_dotenv("config.env", override=True)

NUTRITIONIX_APP_ID = environ.get("NUTRITIONIX_APP_ID")
NUTRITIONIX_APP_KEY = environ.get("NUTRITIONIX_APP_KEY")
GENDER = "male"
WEIGHT_KG = 48
HEIGHT_CM = 167
AGE = 26

SHEETY_WORKOUT_ENDPOINT = environ.get(("SHEETY_WORKOUT_ENDPOINT"))

nutrionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_query = input("Tell me which exercises you did? ")

headers = {"x-app-id": NUTRITIONIX_APP_ID, "x-app-key": NUTRITIONIX_APP_KEY}

nutrionix_params = {
    "query": exercise_query,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

response = requests.post(url=nutrionix_endpoint, json=nutrionix_params, headers=headers)
result = response.json()
# print(result)

current_date = datetime.now().strftime("%d/%m/%Y")
current_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheety_params = {
        "workout": {
            "date": current_date,
            "time": current_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }

    sheet_resp = requests.post(url=SHEETY_WORKOUT_ENDPOINT, json=sheety_params)
    # print(sheet_resp.text)
