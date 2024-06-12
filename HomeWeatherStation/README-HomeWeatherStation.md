# HomeWeatherStation

## Introduction
The HomeWeatherStation project allows you to set up a personal weather station in your backyard, enabling real-time monitoring of temperature and humidity.

## List of Necessary Materials
- Adafruit DHT22 sensor
- Raspberry Pi (or any compatible microcontroller)
- Jumper wires
- Internet connection
- Python 3.x
- Adafruit_DHT library
- Requests library

## Project Purpose
This project aims to provide a simple and cost-effective way to monitor local weather conditions. It is designed for hobbyists, DIY enthusiasts, and anyone interested in tracking weather patterns at home. By using a DHT22 sensor connected to a Raspberry Pi, the system collects temperature and humidity data and uploads it to a server for real-time monitoring and analysis.

## Pros and Cons

### Pros
- Easy to set up and use
- Cost-effective solution for home weather monitoring
- Real-time data collection and monitoring
- Customizable and expandable

### Cons
- Limited to temperature and humidity measurements
- Requires an internet connection for data upload
- Dependent on the reliability of the DHT22 sensor

## General Guidelines

### Installation
1. Install Python 3.x on your Raspberry Pi.
2. Install the Adafruit_DHT library:
    ```bash
    sudo pip install Adafruit_DHT
    ```
3. Install the Requests library:
    ```bash
    sudo pip install requests
    ```

### Usage
1. Connect the DHT22 sensor to your Raspberry Pi following the wiring diagram.
2. Update the `API_ENDPOINT` variable in the script with your server's URL.
3. Run the script:
    ```bash
    python home_weather_station.py
    ```

### Troubleshooting
- Ensure the sensor is properly connected to the Raspberry Pi.
- Verify that the correct GPIO pin is specified in the script.
- Check the internet connection and server URL.

## License
This project is open-source and free to use under the MIT License.
