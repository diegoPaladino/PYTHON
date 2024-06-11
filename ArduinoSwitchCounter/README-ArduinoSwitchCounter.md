# ArduinoSwitchCounter

## Introduction
ArduinoSwitchCounter is a simple Python-based project to register and count switch activations using the EEPROM memory of an Arduino. This project allows you to track the number of times a switch has been activated and retrieve the count via a serial connection.

## Materials Needed
- Arduino Nano
- Switch
- Resistors
- Jumper wires
- Breadboard
- Computer with Python installed
- USB cable for Arduino

## Project Purpose
The purpose of this project is to provide a simple and reliable way to count switch activations using an Arduino and retrieve the data using a Python script. This can be useful for various applications such as tracking user interactions, monitoring equipment usage, or logging events.

## Pros and Cons
### Pros
- Simple and easy to implement
- Uses Arduino's non-volatile EEPROM memory to store data
- Python script allows for easy data retrieval

### Cons
- Limited by EEPROM storage capacity (1024 bytes)
- Suitable for simple counting applications only

## General Instructions
### Arduino Setup
1. Connect the switch to the Arduino Nano as per the circuit diagram.
2. Upload the provided Arduino code to the Arduino Nano.

### Python Script Setup
1. Ensure Python is installed on your computer.
2. Install the `pyserial` library using `pip install pyserial`.
3. Update the serial port in the Python script to match your Arduino's port.
4. Run the Python script to retrieve the count.

### Example Arduino Code
```cpp
#include <EEPROM.h>

const int switchPin = 2;
int counter = 0;

void setup() {
  Serial.begin(9600);
  pinMode(switchPin, INPUT_PULLUP);
  EEPROM.get(0, counter);
}

void loop() {
  static int lastState = HIGH;
  int currentState = digitalRead(switchPin);

  if (lastState == HIGH && currentState == LOW) {
    counter++;
    EEPROM.put(0, counter);
    delay(50);
  }

  lastState = currentState;

  if (Serial.available()) {
    char command = Serial.read();

    if (command == 'r') {
      Serial.print("Count: ");
      Serial.println(counter);
    }
  }
}
