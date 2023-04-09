import os
import requests
from datetime import datetime
from dotenv import load_dotenv

load_dotenv('config.env', override=True)

PIXELA_TOKEN = os.getenv("PIXELA_TOKEN")
PIXELA_UNAME = os.getenv("PIXELA_UNAME")
GRAPH_ID = os.getenv("GRAPH_ID")

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": PIXELA_TOKEN,
    "username": PIXELA_UNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# POST - To Create or Post any date
# Create User Account
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{PIXELA_UNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Coding Graph",
    "unit": "Hour",
    "type": "float",
    "color": "shibafu"
}

headers = {
    "X-USER-TOKEN": PIXELA_TOKEN
}

# Create Graph
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_creation_endpoint = f"{pixela_endpoint}/{PIXELA_UNAME}/graphs/{GRAPH_ID}"

today = datetime.now().strftime("%Y%m%d")
# print(today)

pixel_params = {
    "date" : today,
    "quantity": input("How many hours did you code today? ")
}

# Fix for Pixela's 75% success rate
success = False
while not success:
    response = requests.post(url=pixel_creation_endpoint, json=pixel_params, headers=headers)
    response_data = response.json()
    if response_data['isSuccess'] is False:
        print('Post failed.\nRetrying...')
    else:
        print('Post successful.')
        success = True
# print(response.text)

update_endpoint = f"{pixela_endpoint}/{PIXELA_UNAME}/graphs/{GRAPH_ID}/{today}"

new_pixel_data = {
    "quantity": "5"
}

# PUT - To Update any data
# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)


delete_endpoint = f"{pixela_endpoint}/{PIXELA_UNAME}/graphs/{GRAPH_ID}/{today}"

# DELETE - To delete any data
# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)