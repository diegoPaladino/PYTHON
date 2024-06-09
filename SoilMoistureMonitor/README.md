# SoilMoistureMonitor

## Introduction
SoilMoistureMonitor is a soil moisture measurement system designed for ferns suspended in air. It features a humidity indicator using three LEDs (green, yellow, and red) to show optimal, warning, and urgent soil moisture levels. The system also includes a mini solar panel to recharge the battery.

## List of Necessary Materials
- Adafruit ADS1115 ADC
- MCP3008 Analog-to-Digital Converter
- Green, Yellow, and Red LEDs
- Solar Panel
- Battery
- GPIO Zero Library
- Python 3.x

## Project Purpose
The purpose of this project is to create an automated system that monitors soil moisture levels in a potted fern and provides visual feedback using LEDs. The system ensures the plant is properly watered and can alert the user when the soil is too dry.

## Pros and Cons

### Pros
- Automated soil moisture monitoring
- Visual indicators for easy status checking
- Solar-powered, making it eco-friendly and low-maintenance

### Cons
- Requires initial setup and programming
- Limited to specific plant types (e.g., ferns)

## General Guidelines
1. **Setup the Hardware:**
   - Connect the ADS1115 ADC to the soil moisture sensor.
   - Connect the MCP3008 to the ADC for analog-to-digital conversion.
   - Connect the green, yellow, and red LEDs to GPIO pins 17, 27, and 22, respectively.
   - Connect the solar panel to the battery system.

2. **Install Necessary Libraries:**
   ```bash
   pip install adafruit-ads1x15 gpiozero
