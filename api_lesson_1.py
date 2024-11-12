import requests


URL = "https://wttr.in/"
CITIES = ["Лондон", "Шереметьево", "Череповец"]


def get_weather(city):
    payload = {
        "n": "",
        "T": "",
        "q": "",
        "m": "",
        "M": "",
        "lang": "ru"
    }
    response = requests.get(URL + city, params=payload)
    response.raise_for_status()
    return response.text

def main():
    for city in CITIES:
        weather_report = get_weather(city)
        print(weather_report)


if __name__ == "__main__":
    main()