# Weather Forecast Project

This project provides a Python script to fetch and print weather forecasts for a specified city using the WeatherAPI. Additionally, it includes a metamorphic test to check the consistency of weather forecasts for nearby cities.

## Table of Contents

- [Features](#features)
- [Setup](#setup)
  - [Installation](#installation)
- [Usage](#usage)
  - [Fetch Weather Forecast](#fetch-weather-forecast)
  - [Run the main script](#run-the-main-script)
  - [Run Metamorphic Testing](#run-metamorphic-testing)
- [Explanation of the Metamorphic Test](#explanation-of-the-metamorphic-test)
  - [Definition of Nearby Cities](#definition-of-nearby-cities)
  - [Obtain forecasts](#obtaining-forecasts)
  - [Consistency Check](#consistency-check)
- [Example Output](#example-output)
  - [Weather Forecast](#weather-forecast)
  - [Metamorphic Test](#metamorphic-test)

## Tabela de Conteúdos [Portuguese]

- [Características](#características)
- [Configuração](#configuração)
  - [Instalação](#instalação)
- [Uso](#uso)
  - [Obter Previsão do Tempo](#obter-previsão-do-tempo)
  - [Execução do script principal](#execução-do-script-principal)
  - [Execução do Teste Metamórfico](#execução-do-teste-metamórfico)
- [Explicação do Teste Metamórfico](#explicação-do-teste-metamórfico)
  - [Definição de Cidades Próximas](#definição-de-cidades-próximas)
  - [Obtenção das previsões](#obtenção-das-previsões)
  - [Verificação de Consistência](#verificação-de-consistência)
- [Exemplo de Saída](#exemplo-de-saída)
  - [Previsão do Tempo](#previsão-do-tempo)
  - [Teste Metamórfico](#teste-metamórfico)

## Features

- Fetches weather forecast for a specified city using WeatherAPI.
- Prints the weather forecast details including date, average temperature, and condition.
- Performs a metamorphic test to verify the consistency of forecasts between nearby cities.

## Setup

**Prerequisites**
- Python 3.x

### Installation
1. Clone the repository:
````
git https://github.com/gabrielsants/weather-metamorphic-testing.git
cd weather-metamorphic-testing
````

2. Install the library `requests` with the prompt::

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


## Características

- Busca a previsão do tempo para uma cidade especificada usando a WeatherAPI.
- Imprime os detalhes da previsão do tempo, incluindo data, temperatura média e condição.
- Realiza um teste metamórfico para verificar a consistência das previsões entre cidades próximas.

## Configuração

**Pré-requisitos**
- Python 3.x

### Instalação
1. Clone o repositório:
````
git https://github.com/gabrielsants/weather-metamorphic-testing.git
cd weather-metamorphic-testing
````

2. Instale a biblioteca `requests` com o comando:

`````
pip install requests
`````

3. Obtenha sua chave da API em [WeatherAPI](https://www.weatherapi.com/) e salve-a no arquivo api_key.txt.

## Uso
### Obter Previsão do Tempo
1. Edite `weather_forecast.py` para especificar sua cidade:

`````
city = "São Paulo"
`````

### Execução do script principal:
`````
python weather_forecast.py
`````

### Execução do Teste Metamórfico:
`````
python test_metamorphic_weather_forecast.py
`````

## Explicação do Teste Metamórfico

### Definição de Cidades Próximas:
Selecionamos um conjunto de cidades próximas (São Paulo, Guarulhos e Osasco) para verificar a consistência das previsões.

### Obtenção das previsões:
Para cada cidade, obtemos a previsão do tempo para os próximos 3 dias usando a função `get_weather_forecast`.

### Verificação de Consistência:
1. Para cada dia da previsão, comparamos as temperaturas médias entre as cidades.
2. Se a diferença de temperatura entre as cidades for maior que um limite arbitrário (por exemplo, 2°C), relatamos uma inconsistência.
3. Também verificamos se as condições meteorológicas (descrições de texto) são consistentes entre as cidades. Se houver mais de uma condição diferente para o mesmo dia, relatamos uma inconsistência.
4. Usamos a variável `all_consistent`  para acompanhar se todas as previsões foram consistentes.


Após verificar todos os dias de previsão, imprimimos uma mensagem indicando se o teste foi aprovado (previsões consistentes) ou reprovado (inconsistências encontradas).

## Exemplo de Saída
### Previsão do Tempo
````
Weather forecast for São Paulo:
Date: 2023-05-20, Average Temperature: 22.5°C, Condition: Partly cloudy
Date: 2023-05-21, Average Temperature: 23.0°C, Condition: Sunny
Date: 2023-05-22, Average Temperature: 21.5°C, Condition: Rain
````

### Teste Metamórfico
`````
Inconsistency detected in temperatures for day 2: [22.5, 23.0, 21.5]
Inconsistency detected in conditions for day 2: ['Partly cloudy', 'Sunny', 'Rain']
Metamorphic test failed: Inconsistencies found in weather forecasts between nearby cities.
`````
