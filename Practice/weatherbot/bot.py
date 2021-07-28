input pyowm

owm = pyowm.OWM('', Language = "ru")

place = input("В каком городе искать ?")

observation = owm.weather_at_place('London,GB')
w = observation.get_weather()

print(w)