# DigitalLaserThermometer

## Introduction

The DigitalLaserThermometer is a Python-based project that measures the temperature of an object from a distance of 10 cm using a laser beam. This project utilizes the MLX90614 sensor to provide accurate temperature readings.

## List of Necessary Materials

- Raspberry Pi or compatible microcontroller
- MLX90614 Infrared Temperature Sensor
- Laser pointer (for alignment)
- Breadboard and connecting wires
- Python 3.x
- Adafruit CircuitPython library

## Project Purpose

The purpose of this project is to create a digital thermometer capable of measuring the temperature of objects without physical contact. This is particularly useful in situations where non-invasive temperature measurement is required, such as in industrial applications, food safety, or medical diagnostics.

## Pros and Cons

### Pros

- **Non-contact measurement**: Allows temperature measurement without direct contact with the object.
- **Accuracy**: Provides precise temperature readings.
- **Ease of use**: Simple Python code for easy implementation and modification.

### Cons

- **Distance limitation**: Accurate only at a fixed distance of 10 cm.
- **Environmental sensitivity**: Can be affected by ambient temperature and environmental factors.

## General Guidelines

### Installation

1. **Set up the Raspberry Pi or compatible microcontroller.**
2. **Connect the MLX90614 sensor to the microcontroller as per the wiring diagram.**
3. **Install the necessary Python libraries:**
   ```sh
   pip install adafruit-circuitpython-mlx90614
