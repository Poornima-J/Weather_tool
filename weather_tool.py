import requests
import json
from pprint import pprint

city = input("Enter name of city")
url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid=***Enter your API Key here***&units=metric".format(city)
res = requests.get(url)
data = res.json()
#pprint(data) This is to print the dictionary in a pretty way to understand it better
temp_c = data['main']['temp']
temp_f = temp_c*1.8+32

print("Temperature of {} is {} Celsius".format(city,temp_c))
print("Temperature of {} is {} Fahreinheit".format(city,temp_f))
