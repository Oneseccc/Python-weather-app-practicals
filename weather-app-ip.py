import requests
import math


# ip = input("Enter your IP address : ")
ip = '95.7.159.24'             #kastamonu = '95.7.159.24'  #istanbul = '213.238.188.68'  #izmir = '194.27.177.6'

def get_coordinates():
    url = "https://ip-geolocation-ipwhois-io.p.rapidapi.com/json/"

    querystring = {"ip":ip}

    headers = {
        "X-RapidAPI-Key": "85affdca9amsh6ec11cd6ac78957p1ca1d2jsnb3a52cdca80a",
        "X-RapidAPI-Host": "ip-geolocation-ipwhois-io.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    data = response.json()['city']
    return data

print('Your IP address is :', get_coordinates())

def get_weather():
    # Get the weather data from the API
    q = get_coordinates()
    limit = 1
    url = 'https://api.openweathermap.org/data/2.5/weather?' \
          + 'q=' + q + '&limit=' + str(limit) + '&appid=1693b1e6c708df411c2461aba8291029'

    payload = {'units': 'metric', 'city': 'name', 'list.weather.main': ''}

    response = requests.request("GET", url, params=payload)

    data = response.json()['main']['temp']
    data2 = response.json()['main']['feels_like']
    data3 = response.json()['weather'][0]['description']
    data4 = response.json()['wind']['speed']
    return  "degree:", round(data),"feels like:", round(data2), data3,"wind speed:", data4


print(get_weather(), get_coordinates())




