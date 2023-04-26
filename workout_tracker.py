import requests
from datetime import datetime
GENDER = "male"
WEIGHT = 82
HEIGHT = 152
AGE = 23
#-------------------------Date -----------------------
time = datetime.now()
to_day = time.strftime("%d/%m/%Y")
time = time.strftime("%X")

#-------------------------Nutritionix API-------------

nutri_app_id = ""

nutri_app_key = ""

header_s = {
    "x-app-id": nutri_app_id,
    "x-app-key": nutri_app_key,
}
query = input("Tell us about  your day...")

post_config = {
    "query": query,
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE,
}

response = requests.post(url="https://trackapi.nutritionix.com/v2/natural/exercise", json=post_config, headers=header_s)
nutri_data = response.json()

exer_cise = nutri_data['exercises'][0]

e_name = exer_cise['name']
e_duration = exer_cise['duration_min']
e_calories = exer_cise['nf_calories']


#-----------------------------Sheety API-------------------

sheety_header = {
    "Authorization": " ",
    "Content-Type": "application/json",
}

sheety_config={
    "workout":{
        "date": to_day,
        "time": time,
        "exercise": f"{e_name.title()}",
        "duration": e_duration,
        "calories": e_calories,
    }
}

response = requests.post(url="https://api.sheety.co/     ", headers=sheety_header, json=sheety_config)
print(response.text)
