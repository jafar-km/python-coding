import requests
from datetime import datetime

USERNAME = "blah"
TOKEN = "hmm"
GRAPH_ID = "graph5"
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token" : TOKEN,
    "username" : USERNAME,
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes",
}


# response = requests.post(pixela_endpoint, json=user_params)


graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name" : "Reading Graph",
    "unit": "pages",
    "type" : "int",
    "color": "sora",


}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(graph_endpoint, json=graph_config, headers=headers)


post_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"


today = datetime(year=2026, month=9, day=30)

pixel_config = {
    "date" : today.strftime("%Y%m%d"),
    "quantity": "20",

}
response = requests.post(post_pixel_endpoint, json=pixel_config, headers=headers)
print(response.text)