import requests

def get_api_key(file_path):
    with open(file_path, 'r') as file:
        return file.read().strip()

def get_weather_forecast(city, api_key, days=3):
    url = f"http://api.weatherapi.com/v1/forecast.json?key={api_key}&q={city}&days={days}"
    response = requests.get(url)
    data = response.json()

    if response.status_code != 200:
        print(f"Erro ao obter dados: {data.get('error', {}).get('message', 'Desconhecido')}")
        return None
    
    forecast_days = data['forecast']['forecastday']
    return forecast_days

def print_forecast(city, forecast):
    print(f"Previsão do tempo para {city}:")
    for day in forecast:
        date = day['date']
        temp_day = day['day']['avgtemp_c']
        condition = day['day']['condition']['text']
        print(f"Data: {date}, Temperatura média: {temp_day}°C, Condição: {condition}")

if __name__ == "__main__":
    api_key = get_api_key('api_key.txt')
    city = "São Paulo"
    
    forecast = get_weather_forecast(city, api_key)
    if forecast:
        print_forecast(city, forecast)
