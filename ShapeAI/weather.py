import requests
from datetime import datetime
api_key='d222523c9704ecc19ebca0a45c0f1811'
location = input("Enter the city name:")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

temp_city=((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd=api_data['wind']['speed']
data_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

print("----------------------------------------------------------------------------------------")
print("Wheather States for - {} || {}".format(location.upper(),data_time))
print("----------------------------------------------------------------------------------------")

print("Current Temprature is: {:.2f} deg C".format(temp_city))
print("Current weather desc :",weather_desc)
print("Current Hummidity:",hmdt,'%')
print("Current wind speed:",wind_spd,'kmph')

with open('weather.text','w') as f:
    f.write("----------------------------------------------------------------------------------------")
    f.write("\nWheather States for - {} || {}".format(location.upper(),data_time))
    f.write("\n----------------------------------------------------------------------------------------")
    f.write("\nCurrent Temprature is: {:.2f} deg C".format(temp_city))
    f.write("\nCurrent weather desc :{}".format(weather_desc))
    f.write("\nCurrent Hummidity: {} %".format(hmdt))
    f.write("\nCurrent wind speed:{}".format(wind_spd))

print("Details successfully saved as a text file")

