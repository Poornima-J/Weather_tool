import requests
import json
import emoji
from pprint import pprint

city = input("Enter name of city")
url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid=***Enter your API Key here***&units=metric".format(city)
res = requests.get(url)
data = res.json()
#pprint(data) This is to print the dictionary in a pretty way to understand it better
temp_c = data['main']['temp']
temp_f = temp_c*1.8+32
weather = data['weather'][0]['main']
if weather == 'clear':
    emoj = ':Sun:'
elif weather == 'Thunderstorm':
    emoj = ':Cloud With Rain:'
elif weather == 'Drizzle':
    emoj = ':Sun Behind Rain Cloud:'
elif weather == 'Rain':
    emoj = ':Umbrella With Rain Drops:'
elif weather == 'Snow':
    emoj = ':Cloud With Snow:'
elif weather == 'Clouds':
    emoj = ':Cloud:'                 

print("Temperature of {} is {} Celsius".format(city,temp_c))
print("Temperature of {} is {} Fahreinheit".format(city,temp_f))
print("Weather is:{}".format(emoji.emojize(emoj)))
