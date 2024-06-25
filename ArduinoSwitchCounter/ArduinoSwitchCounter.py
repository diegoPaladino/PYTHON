"""
Arduino Switch Counter - Register switch activations using Arduino's EEPROM
"""

import serial

class ArduinoSwitchCounter:
    def __init__(self, port, baudrate=9600):
        self.port = port
        self.baudrate = baudrate
        self.serial_connection = serial.Serial(self.port, self.baudrate)

    def read_count(self):
        self.serial_connection.write(b'r')
        count = self.serial_connection.readline().decode('utf-8').strip()
        return int(count.split(":")[1].strip())

    def close(self):
        self.serial_connection.close()


if __name__ == "__main__":
    arduino_counter = ArduinoSwitchCounter(port='/dev/ttyUSB0')  # Update port as needed
    try:
        count = arduino_counter.read_count()
        print(f"Current count: {count}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        arduino_counter.close()
        
# code to implementation in a secretary's door
# starting work in 25, June
