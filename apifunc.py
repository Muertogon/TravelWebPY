import requests
def whatCityWeather(city):
    url = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=4ebb48b17238d755e6e5120b459fde06&units=metric"
    response = requests.get(url)
    
    if response.status_code == 200:
        x = response.json()['weather'][0]['main']
    return x