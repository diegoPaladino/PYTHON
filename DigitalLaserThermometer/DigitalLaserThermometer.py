import time
import board
import adafruit_mlx90614
import busio

class DigitalLaserThermometer:
    def __init__(self, sensor_address=0x5A):
        self.i2c = busio.I2C(board.SCL, board.SDA)
        self.sensor = adafruit_mlx90614.MLX90614(self.i2c, address=sensor_address)

    def get_object_temperature(self):
        return self.sensor.object_temperature

    def get_ambient_temperature(self):
        return self.sensor.ambient_temperature

def main():
    thermometer = DigitalLaserThermometer()
    
    while True:
        object_temp = thermometer.get_object_temperature()
        ambient_temp = thermometer.get_ambient_temperature()
        print(f"Object Temperature: {object_temp:.2f} °C")
        print(f"Ambient Temperature: {ambient_temp:.2f} °C")
        time.sleep(2)

if __name__ == "__main__":
    main()
