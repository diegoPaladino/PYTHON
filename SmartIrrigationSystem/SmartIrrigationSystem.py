import time
import RPi.GPIO as GPIO

class SmartIrrigationSystem:
    def __init__(self, moisture_sensor_pin, pump_pin, threshold):
        self.moisture_sensor_pin = moisture_sensor_pin
        self.pump_pin = pump_pin
        self.threshold = threshold
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.moisture_sensor_pin, GPIO.IN)
        GPIO.setup(self.pump_pin, GPIO.OUT)

    def read_moisture(self):
        return GPIO.input(self.moisture_sensor_pin)

    def water_plants(self):
        GPIO.output(self.pump_pin, GPIO.HIGH)
        print("Watering plants...")
        time.sleep(10)
        GPIO.output(self.pump_pin, GPIO.LOW)
        print("Watering done.")

    def run(self):
        try:
            while True:
                moisture_level = self.read_moisture()
                if moisture_level < self.threshold:
                    self.water_plants()
                else:
                    print("Soil moisture is sufficient.")
                time.sleep(60)
        except KeyboardInterrupt:
            GPIO.cleanup()
            print("System stopped.")

if __name__ == "__main__":
    system = SmartIrrigationSystem(moisture_sensor_pin=17, pump_pin=18, threshold=500)
    system.run()
