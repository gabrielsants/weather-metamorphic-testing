# Weather Forecast Project

This project provides a Python script to fetch and print weather forecasts for a specified city using the WeatherAPI. Additionally, it includes a metamorphic test to check the consistency of weather forecasts for nearby cities.

## Features

- Fetches weather forecast for a specified city using WeatherAPI.
- Prints the weather forecast details including date, average temperature, and condition.
- Performs a metamorphic test to verify the consistency of forecasts between nearby cities.

## Setup

**Prerequisites**
- Python 3.x
- `requests` library

### Installation
1. Clone the repository:
````
git https://github.com/gabrielsants/weather-metamorphic-testing.git
cd weather-metamorphic-testing
````

2. Install the required library:

`````
pip install requests
`````

3. Get your API key from [WeatherAPI](https://www.weatherapi.com/) and save it in api_key.txt.

## Usage
### Fetch Weather Forecast
1. Edit `weather_forecast.py` to specify your city:

`````
city = "São Paulo"
`````

### Run the main script:
`````
python weather_forecast.py
`````

### Run Metamorphic Testing:
`````
python test_metamorphic_weather_forecast.py
`````

## Explanation of the Metamorphic Test

### Definition of Nearby Cities:
We selected a set of nearby cities (São Paulo, Guarulhos and Osasco) to check the consistency of the forecasts.

### Obtaining forecasts:
For each city, we get the weather forecast for the next 3 days using the `get_weather_forecast` function.

### Consistency Check:
1. For each day of the forecast, we compare the average temperatures between the cities.
2. If the temperature difference between the cities is greater than an arbitrary threshold (e.g. 2°C), we report an inconsistency.
3. We also check that the weather conditions (text descriptions) are consistent between the cities. If there is more than one different condition for the same day, we report an inconsistency.
4. We use the `all_consistent` variable to track whether all forecasts were consistent.


After checking all the forecast days, we print out a message indicating whether the test passed (consistent forecasts) or failed (inconsistencies found).

## Example Output
### Weather Forecast
````
Weather forecast for São Paulo:
Date: 2023-05-20, Average Temperature: 22.5°C, Condition: Partly cloudy
Date: 2023-05-21, Average Temperature: 23.0°C, Condition: Sunny
Date: 2023-05-22, Average Temperature: 21.5°C, Condition: Rain
````

### Metamorphic Test
`````
Inconsistency detected in temperatures for day 2: [22.5, 23.0, 21.5]
Inconsistency detected in conditions for day 2: ['Partly cloudy', 'Sunny', 'Rain']
Metamorphic test failed: Inconsistencies found in weather forecasts between nearby cities.
`````
