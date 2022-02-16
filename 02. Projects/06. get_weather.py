# openweathermap.org -> get free API by creating an account here

# pip install requests

import requests

API_KEY = "f88017efd71e311d9a259c6ab04dbc5a"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def weather_run():

    city = input("Enter city: ")

    url = f"{BASE_URL}?appid={API_KEY}&q={city}"
    # print(url)

    response = requests.get(url)
    # print(response) -> 200, 404, etc
    try:
        data = response.json()
        # print(data)
        weather = data['weather'][0]['description']
        print(f"Weather: {weather}")

        temperature = data['main']['temp'] - 273.15
        print(f"Temperature: {round(temperature, 2)}\u00b0C")

        country = data['sys']['country']
        print(f"Country: {country}")

        city_name = data['name']
        print(f"City name: {city_name}")

    except KeyError:
        code = data['cod']
        msg = data['message']
        # print(f"Error code: {code}\nError message: {msg}")
        print(f"Oops! {msg}")

weather_run()

while True:

    brorcont = input("Continue or quit? (c/q): ").lower()

    if brorcont == "c":
        weather_run()

    elif brorcont == "q":
        print("Program terminated")
        quit()

    else:
        print("Invalid option, try again.")
        continue

# Alternate method: using conditional statements instead of try/except:

# if response.status_code == 200:
#     data = response.json()
#     # print(data)
#     weather = data['weather'][0]['description']
#     print(f"Weather: {weather}")
#
#     temperature = data['main']['temp'] - 273.15
#     print(f"Temperature: {round(temperature, 2)}\u00b0C")
#
#     country = data['sys']['country']
#     print(f"Country: {country}")
#
# else:
#     print("Error occurred")
