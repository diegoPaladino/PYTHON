import time
import random

class GasSensor:
    def __init__(self, threshold):
        self.threshold = threshold
    
    def read_gas_level(self):
        # Simulate reading gas level
        return random.uniform(0, 100)

class GasLeakDetector:
    def __init__(self, sensor, alarm):
        self.sensor = sensor
        self.alarm = alarm

    def monitor(self):
        while True:
            gas_level = self.sensor.read_gas_level()
            print(f"Gas Level: {gas_level}")
            if gas_level > self.sensor.threshold:
                self.alarm.trigger()
            time.sleep(1)

class Alarm:
    def trigger(self):
        print("Gas leak detected! Triggering alarm...")

def main():
    threshold = 50.0  # Set your threshold level
    gas_sensor = GasSensor(threshold)
    alarm = Alarm()
    detector = GasLeakDetector(gas_sensor, alarm)
    
    try:
        detector.monitor()
    except KeyboardInterrupt:
        print("Monitoring stopped.")

if __name__ == "__main__":
    main()
