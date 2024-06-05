# AirQualityMonitor

## Introduction
The AirQualityMonitor project is designed to continuously monitor and report air quality metrics, specifically temperature and humidity, using a DHT22 sensor and a Raspberry Pi.

## Materials Needed
- Raspberry Pi (any model with GPIO support)
- DHT22 sensor
- Jumper wires
- Breadboard (optional)

## Project Purpose
This project aims to provide a simple and effective solution for monitoring air quality in indoor environments. It was created to help individuals and organizations maintain optimal air conditions for health and comfort. Potential beneficiaries include home users, office managers, and small businesses.

## Pros and Cons
### Pros
- Easy to set up and use
- Provides real-time monitoring
- Low-cost components

### Cons
- Limited to temperature and humidity monitoring
- Requires basic knowledge of Raspberry Pi and Python

## General Instructions
1. **Hardware Setup:**
   - Connect the DHT22 sensor to the Raspberry Pi.
   - Pin 1 (VCC) -> 3.3V
   - Pin 2 (Data) -> GPIO4
   - Pin 4 (GND) -> GND

2. **Software Setup:**
   - Ensure Python is installed on your Raspberry Pi.
   - Install the Adafruit_DHT library using:
     ```sh
     sudo pip install Adafruit_DHT
     ```

3. **Running the Project:**
   - Clone the repository:
     ```sh
     git clone https://github.com/yourusername/AirQualityMonitor.git
     ```
   - Navigate to the project directory:
     ```sh
     cd AirQualityMonitor
     ```
   - Run the monitoring script:
     ```sh
     python air_quality_monitor.py
     ```

## License
This project is licensed under the MIT License. Feel free to use, modify, and distribute as you see fit.

