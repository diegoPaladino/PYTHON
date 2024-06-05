import time
import Adafruit_DHT

# Constants
SENSOR = Adafruit_DHT.DHT22
PIN = 4

# Function to read data from the sensor
def read_air_quality():
    humidity, temperature = Adafruit_DHT.read_retry(SENSOR, PIN)
    if humidity is not None and temperature is not None:
        return {'temperature': temperature, 'humidity': humidity}
    else:
        return None

# Main monitoring function
def monitor_air_quality(interval=60):
    while True:
        data = read_air_quality()
        if data:
            print(f"Temperature: {data['temperature']:.2f} C  Humidity: {data['humidity']:.2f} %")
        else:
            print("Failed to retrieve data from the sensor")
        time.sleep(interval)

if __name__ == "__main__":
    monitor_air_quality()
