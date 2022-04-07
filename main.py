import requests
import urllib


def getLonLat(locality):
    url = 'https://nominatim.openstreetmap.org/search/' + \
        urllib.parse.quote(locality) + '?format=json'
    response = requests.get(url).json()
    if (len(response) > 0):
        geoLocation = {
            "lat": response[0]["lat"],
            "lon": response[0]["lon"],
        }

        return geoLocation
    else:
        return -1


def getWeather(geoLocation):
    if (geoLocation != -1):
        lat = geoLocation["lat"]
        lon = geoLocation["lon"]
        url = 'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api}'.format(
            lat=lat, lon=lon, api="2e7be0b91b0dfd9db480f32aade9560f")
        response = requests.get(url).json()
        filteredResponse = {
            "weather": response["weather"],
            "main": response["main"],
        }

        return filteredResponse
    else:
        return -1


locationSubCity = input("Write the location subcity: ").strip()
locationCity = input("Write the location city: ").strip()
locationCountry = input("Write the location country: ").strip()

if (locationSubCity == ""):
    location = locationCity + ", " + locationCountry
else:
    location = locationSubCity + ", " + locationCity + ", " + locationCountry


def displayWeather(weather):
    if (weather != -1):
        description = weather["weather"][0]["description"]
        temperature = weather["main"]["temp"]
        humidity = weather["main"]["humidity"]

        output = "\nThe weather description is {description} with a temperature of {temperature}°c and a humidity of {humidity}\n".format(
            description=description, temperature=float("{:.2f}".format(temperature-272.15)), humidity=humidity)
        print(output)
    else:
        print("\nAn Error has occurred!\n")


displayWeather(
    getWeather(
        getLonLat(location)
    )
)
