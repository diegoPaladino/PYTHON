import time
import random

class FireAlarmSystem:
    def __init__(self, threshold=70):
        self.threshold = threshold

    def read_sensor_data(self):
        # Simulate reading data from a temperature sensor
        return random.uniform(20, 100)

    def check_for_fire(self):
        temperature = self.read_sensor_data()
        print(f"Current Temperature: {temperature:.2f}°C")
        if temperature > self.threshold:
            self.trigger_alarm()
        else:
            print("No fire detected.")

    def trigger_alarm(self):
        print("!!! FIRE DETECTED !!! Evacuate immediately!")

def main():
    system = FireAlarmSystem()
    while True:
        system.check_for_fire()
        time.sleep(5)  # Check every 5 seconds

if __name__ == "__main__":
    main()
