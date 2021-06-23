import requests


class Weather:

    @staticmethod
    def show_weather(city):
        api_key = ""
        r = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}")
        if r:
            data = {
                "Name": r.json()["name"],
                "Description": r.json()["weather"][0]["description"],
                "Temp": round(r.json()["main"]["temp"] - 273.15, 2)
            }
            city_name = data["Name"]
            city_description = data["Description"]
            city_temp = data["Temp"]
            return f"{city_name} {city_description} {city_temp}℃"
        else:
            return "Wprowadziłeś złe miasto!"