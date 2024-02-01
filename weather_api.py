import requests
import math

# Get the weather data from the API
q = input("Enter the city name: ")
limit = 1


url= 'https://api.openweathermap.org/data/2.5/weather?' \
        + 'q=' + q + '&limit=' + str(limit) + '&appid=1693b1e6c708df411c2461aba8291029'


payload = {'units': 'metric', 'city': 'name', 'list.weather.main': ''}



response = requests.request("GET", url,  params=payload)


data = response.json()['main']['temp']
data2 = response.json()['main']['feels_like']
data3 = response.json()['weather'][0]['description']
data4 = response.json()['wind']['speed']



print('Temperature :', math.ceil(data), 'Degrees') # Print the temperature
print('Feels like :', math.ceil(data2), 'degrees') # Print the feels like temperature
print('Weather condition :', data3) # Print the weather description
print('Wind speed :', data4 ,'km\h') # Print the wind speed
