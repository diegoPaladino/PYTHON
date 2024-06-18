# HomeEnergyMonitor

## Introduction
HomeEnergyMonitor is an IoT-based system designed to monitor the electrical energy consumption at each point in your home. It measures the consumption in amperes and stores the data for analysis.

## List of Necessary Materials
- IoT energy monitoring devices capable of measuring current (amperage) and publishing data via MQTT
- A computer or server running Python
- MQTT broker (e.g., Mosquitto)
- SQLite3 (included with Python)

## Project Purpose
The purpose of this project is to provide real-time monitoring of electrical energy consumption in a household. It helps in identifying high consumption points and managing energy usage efficiently.

## Pros and Cons
### Pros
- Real-time energy monitoring
- Data storage for historical analysis
- Scalable to many points of measurement
### Cons
- Requires MQTT-enabled energy monitoring devices
- Dependent on network stability

## General Guidelines
### Setup
1. Install the required Python libraries:
    ```sh
    pip install paho-mqtt
    ```
2. Configure your MQTT broker and energy monitoring devices to publish to the topic `home/energy`.

### Running the Project
1. Set up your SQLite database by running the script:
    ```sh
    python home_energy_monitor.py
    ```
2. The script will automatically subscribe to the MQTT topic and start receiving and storing data.

### License
This project is licensed under the MIT License.
