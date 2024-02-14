# TilapiaTechFeeder

## Introduction
TilapiaTechFeeder is a Python-based project utilizing LoRa technology for smart fish farming, focusing on tilapia. It automates feeding based on predefined conditions and monitors water quality parameters such as temperature and humidity.

## List of Necessary Materials
- Raspberry Pi (or any compatible microcontroller with GPIO pins)
- DHT22 temperature and humidity sensor
- Relay Module
- LoRa RFM95W Transceiver Module
- Jumper wires

## Project Purpose
This project aims to improve tilapia farming efficiency by ensuring optimal feeding times and monitoring environmental conditions. It is designed for aquaculture enthusiasts, researchers, and commercial fish farmers to enhance productivity and fish welfare.

## Pros and Cons
**Pros:**
- Automated feeding reduces manual labor.
- Real-time environmental monitoring.
- Uses LoRa for long-range, low-power communication.

**Cons:**
- Requires initial setup and calibration.
- Dependent on external power supply.
- Limited by LoRa network coverage.

## General Guidelines
1. Assemble the hardware according to the wiring diagram provided in the source code comments.
2. Install the necessary Python libraries: `adafruit_dht`, `digitalio`, and `adafruit_lorafi`.
3. Adjust the feeding and environmental conditions checking logic as per your requirements.
4. Deploy the script to run automatically on your microcontroller.

## License
This project is open-sourced under the MIT License. Feel free to use, modify, and distribute as per the license terms.

