import requests
import json
from pprint import pprint

city = input("Enter name of city")
url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid=***Enter your API Key here***".format(city)
res = requests.get(url)
data = res.json()
#pprint(data) This is to print the dictionary in a pretty way to understand it better
temp_k = data['main']['temp']

print("Temperature of {} is {} kelvin".format(city,temp_k))
