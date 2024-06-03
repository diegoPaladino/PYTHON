import time
import Adafruit_DHT

class SoilMoistureSensor:
    def __init__(self, pin, threshold):
        self.pin = pin
        self.threshold = threshold

    def read_moisture(self):
        humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, self.pin)
        return humidity

    def is_moisture_below_threshold(self):
        return self.read_moisture() < self.threshold

class IrrigationSystem:
    def __init__(self, sensor, pump_pin):
        self.sensor = sensor
        self.pump_pin = pump_pin

    def water_lawn(self):
        print("Starting irrigation system...")
        # GPIO.output(self.pump_pin, GPIO.HIGH)  # Uncomment for actual GPIO control
        time.sleep(10)  # Water for 10 seconds
        # GPIO.output(self.pump_pin, GPIO.LOW)  # Uncomment for actual GPIO control
        print("Irrigation complete.")

    def run(self):
        while True:
            if self.sensor.is_moisture_below_threshold():
                self.water_lawn()
            else:
                print("Soil moisture is sufficient.")
            time.sleep(60)  # Check every minute

def main():
    moisture_sensor = SoilMoistureSensor(pin=4, threshold=40)
    irrigation_system = IrrigationSystem(sensor=moisture_sensor, pump_pin=17)
    irrigation_system.run()

if __name__ == "__main__":
    main()
