# Simple Weather Forecast using Logical Operators

# Take inputs
temperature = float(input("Enter temperature in °C: "))
humidity = float(input("Enter humidity (%): "))
wind_speed = float(input("Enter wind speed (km/h): "))

# Forecast logic
if temperature > 30 and humidity > 60:
    print("🌧️ High chance of Rain (Hot & Humid).")
elif temperature < 10 and wind_speed > 20:
    print("❄️ Cold and Windy - Possible Snow or Chill.")
elif 20 <= temperature <= 30 and humidity < 50:
    print("☀️ Pleasant and Sunny day.")
elif temperature > 35 and wind_speed < 10:
    print("🔥 Very Hot - Stay Hydrated!")
elif humidity > 80 and wind_speed > 15:
    print("🌪️ Possible Stormy Weather!")
else:
    print("🌤️ Normal Weather - No extreme conditions.")
