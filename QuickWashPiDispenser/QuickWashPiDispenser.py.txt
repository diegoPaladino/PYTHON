import RPi.GPIO as GPIO
import time

class QuickWashDispenser:
    def __init__(self, motor_pin):
        self.motor_pin = motor_pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.motor_pin, GPIO.OUT)

    def dispense_soap(self, duration=1):
        GPIO.output(self.motor_pin, GPIO.HIGH)
        time.sleep(duration)
        GPIO.output(self.motor_pin, GPIO.LOW)

    def cleanup(self):
        GPIO.cleanup()

if __name__ == "__main__":
    dispenser = QuickWashDispenser(motor_pin=18)  # Define the GPIO pin for the motor
    try:
        while True:
            input("Press Enter to dispense soap...")
            dispenser.dispense_soap(duration=1)  # Dispenses soap for 1 second
    except KeyboardInterrupt:
        print("Program stopped by the user")
    finally:
        dispenser.cleanup()
