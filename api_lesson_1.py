import requests


BASE_URL = "https://wttr.in/{}?nTqmM&lang=ru"
CITIES = ["Лондон", "Шереметьево", "Череповец"]


def get_weather(city):
    url = BASE_URL.format(city)
    response = requests.get(url)
    response.raise_for_status()
    return response.text

def main():
    for city in CITIES:
        weather_report = get_weather(city)
        print(weather_report)

if __name__ == "__main__":
    main()
