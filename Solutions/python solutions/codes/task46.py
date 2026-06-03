import requests
class WeatherFetcher:
    def __init__(self, lat, lon):
        self.url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"

    def fetch_weather(self):
        try:
            response = requests.get(self.url, timeout=10)
            response.raise_for_status()
            data = response.json()
            if "current_weather" in data:
                cw = data["current_weather"]
                temp = cw["temperature"]
                code = cw["weathercode"]
                print(f"Temperature: {temp}°C")
                print(f"Weather Code: {code}")
            else:
                print("Error: Invalid response format.")
        except requests.exceptions.HTTPError as http_err:
            if response.status_code == 404:
                print("Error 404: Weather service endpoint not found.")
            else:
                print(f"HTTP Error: {http_err}")
        except requests.exceptions.RequestException as req_err:
            print(f"Network Error: {req_err}")

fetcher = WeatherFetcher(52.52, 13.41)
fetcher.fetch_weather()
