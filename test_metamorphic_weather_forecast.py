# test_weather_forecast.py

from weather_forecast import get_weather_forecast

def get_api_key(file_path):
    with open(file_path, 'r') as file:
        return file.read().strip()

def test_metamorphic_weather_forecast(api_key):
    cities = ["São Paulo", "Guarulhos", "Osasco"]
    
    forecasts = {}
    for city in cities:
        forecasts[city] = get_weather_forecast(city, api_key)
    
    all_consistent = True
    
    for day_index in range(3):
        temp_values = []
        conditions = []
        for city in cities:
            forecast = forecasts[city]
            if forecast is not None:
                temp_values.append(forecast[day_index]['day']['avgtemp_c'])
                conditions.append(forecast[day_index]['day']['condition']['text'])
        
        temp_diff = max(temp_values) - min(temp_values)
        #If the temperature difference between the cities is greater than an arbitrary threshold (e.g. 2°C), we report an inconsistency.
        #This is your metamorphic relation
        if temp_diff > 2:
            print(f"Inconsistência detectada nas temperaturas para o dia {day_index + 1}: {temp_values}")
            all_consistent = False
        
        if len(set(conditions)) > 1:
            print(f"Inconsistência detectada nas condições para o dia {day_index + 1}: {conditions}")
            all_consistent = False

    if all_consistent:
        print("Teste metamórfico passou: As previsões são consistentes entre as cidades próximas.")
    else:
        print("Teste metamórfico falhou: Inconsistências encontradas nas previsões entre as cidades próximas.")

if __name__ == "__main__":
    api_key = get_api_key('api_key.txt')
    test_metamorphic_weather_forecast(api_key)
