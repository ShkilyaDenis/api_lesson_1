import requests


URL = "https://wttr.in/"
CITIES = ["Лондон", "Шереметьево", "Череповец"]
PAYLOAD = {
        "n": "",
        "T": "",
        "q": "",
        "m": "",
        "M": "",
        "lang": "ru"
    }


def get_weather(city):
    response = requests.get(URL + city, params=PAYLOAD)
    response.raise_for_status()
    return response.text

def main():
    for city in CITIES:
        weather_report = get_weather(city)
        print(weather_report)


if __name__ == "__main__":
    main()