# CodeVedX_task4
Weather App

A simple desktop weather application built with Python and the Tkinter library. Enter a city name to view its current weather information, including temperature, conditions, humidity, and wind speed.

## Features

- User-friendly Tkinter graphical interface
- Search current weather by city name
- Displays temperature, weather condition, humidity, and wind speed
- Uses a weather API for live data
- Handles invalid city names and network errors

## Requirements

- Python 3.x
- Tkinter (included with most Python installations)
- `requests` library
- An API key from a weather-data provider, such as OpenWeatherMap

## Installation

1. Clone or download this project.
2. Install the required package:

   ```bash
   pip install requests
   ```

3. Create an account at [OpenWeatherMap](https://openweathermap.org/api) and generate an API key.
4. Add your API key to the Python source file:

   ```python
   API_KEY = "your_api_key"
   ```

## Usage

Run the application from a terminal:

```bash
python weather_app.py
```

Type a city name in the input field and click **Search** (or the app's weather button). The current weather details will appear in the window.

## Example Output

```text
City: Mumbai
Temperature: 29°C
Weather: Clear sky
Humidity: 78%
```

## Technologies Used

- Python
- Tkinter
- Requests
- Weather API

## Error Handling

The application shows an appropriate message if:

- The city name is invalid or not found
- The API key is missing or invalid
- An internet connection is unavailable
- The weather service cannot be reached

## Learning Outcomes

This project demonstrates Python GUI programming with Tkinter, API integration, JSON response handling, and basic exception handling.

## License

This project is intended for educational use.
