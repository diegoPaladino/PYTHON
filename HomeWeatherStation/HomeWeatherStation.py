import Adafruit_DHT
import time
import requests

# Constants
DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4
API_ENDPOINT = "http://example.com/upload_data"

# Function to read sensor data
def read_sensor():
    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
    return humidity, temperature

# Function to send data to server
def send_data(humidity, temperature):
    payload = {
        'temperature': temperature,
        'humidity': humidity
    }
    response = requests.post(API_ENDPOINT, json=payload)
    return response.status_code

# Main function
def main():
    while True:
        humidity, temperature = read_sensor()
        if humidity is not None and temperature is not None:
            status_code = send_data(humidity, temperature)
            if status_code == 200:
                print(f"Data sent successfully: Temp={temperature:.2f}C, Humidity={humidity:.2f}%")
            else:
                print("Failed to send data")
        else:
            print("Failed to retrieve data from sensor")
        time.sleep(60)

if __name__ == "__main__":
    main()
