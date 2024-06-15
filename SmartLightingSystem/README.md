# SmartLightingSystem

## Introduction
The SmartLightingSystem is an intelligent lighting solution for your garage and garden. It automatically turns on the lights when motion is detected, providing convenience and energy efficiency.

## List of Necessary Materials
- Raspberry Pi
- PIR Motion Sensors (2 units)
- Relay Modules (2 units)
- Light Fixtures (2 units)
- Jumper Wires
- Power Supply

## Project Purpose
The purpose of this project is to create an automated lighting system that enhances the security and convenience of your garage and garden areas by automatically activating the lights when motion is detected.

## Pros and Cons
### Pros
- Automated lighting enhances security.
- Energy-efficient as lights are only on when needed.
- Convenient for users entering the garage or garden at night.

### Cons
- Initial setup requires basic knowledge of electronics and programming.
- Dependent on the proper functioning of sensors and Raspberry Pi.

## General Guidelines
### Installation
1. **Hardware Setup:**
   - Connect the PIR sensors to the designated GPIO pins on the Raspberry Pi.
   - Connect the relay modules to control the light fixtures.
   - Ensure all connections are secure and powered correctly.

2. **Software Setup:**
   - Install the RPi.GPIO library using `pip install RPi.GPIO`.
   - Download and run the Python script provided.

### Usage
- Ensure the Raspberry Pi is powered on and the script is running.
- The system will automatically turn on the lights in the garage or garden when motion is detected by the respective sensors.

### Troubleshooting
- If the lights do not turn on, check the sensor connections.
- Ensure the Raspberry Pi GPIO pins are correctly configured.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
