# Automated Lawn Irrigation System

## Introduction
The Automated Lawn Irrigation System is designed to automatically water your lawn based on soil moisture levels instead of a fixed schedule. This ensures your lawn receives the right amount of water, conserving water and promoting healthy grass growth.

## List of Necessary Materials
- Raspberry Pi
- Adafruit DHT22 sensor
- Relay module
- Water pump
- Jumper wires
- Breadboard
- Power supply

## Project Purpose
The purpose of this project is to automate the irrigation of your lawn by using a soil moisture sensor to determine when watering is needed. This system helps to prevent overwatering or underwatering, ensuring optimal lawn health and water usage efficiency. It is ideal for homeowners who want to maintain their lawns with minimal manual effort.

## Pros and Cons
### Pros
- Automated watering based on soil moisture
- Water conservation
- Promotes healthy lawn growth
- Reduces manual labor

### Cons
- Initial setup and calibration required
- Dependency on sensor accuracy
- Requires Raspberry Pi and additional hardware

## General Guidelines
### Installation
1. Assemble the hardware components as per the circuit diagram.
2. Connect the DHT22 sensor to the Raspberry Pi.
3. Connect the relay module to control the water pump.
4. Install the necessary Python libraries:
    ```bash
    pip install Adafruit_DHT
    ```
5. Upload and run the `irrigation_system.py` script on your Raspberry Pi.

### Usage
- The system continuously monitors the soil moisture level.
- If the moisture level is below the threshold, the water pump is activated to water the lawn for a specified duration.

### Troubleshooting
- Ensure all connections are secure.
- Calibrate the moisture threshold as per your soil type.
- Check the power supply for the water pump.

## License
This project is open-source and free to use. Feel free to modify and distribute as per your needs.

---

### Download Link for README.md
[Download README.md](sandbox:/mnt/data/README.md)

### D. Título do Commit

`Add Automated Lawn Irrigation System`

### E. Descrição do Commit

Implemented the initial version of the Automated Lawn Irrigation System. This system uses a soil moisture sensor to automate the irrigation process, ensuring efficient water usage and promoting healthy lawn growth.

### F. Imagem de Logomarca

![Automated Lawn Irrigation System Logo](sandbox:/mnt/data/automated_lawn_irrigation_system_logo.png)
