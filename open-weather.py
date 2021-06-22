import requests

API='http://api.openweathermap.org/data/2.5/weather?appid=dc551f260e1043a60d180da6b65be5c9&q='

City = input('Ciudad= ')

url = API + City

json_data = requests.get(url).json()

print("Datos actuales del clima:",json_data)