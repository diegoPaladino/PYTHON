import RPi.GPIO as GPIO
import time

# Define the GPIO pins for sensors and actuators
garage_sensor_pin = 18
garden_sensor_pin = 23
garage_light_pin = 24
garden_light_pin = 25

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(garage_sensor_pin, GPIO.IN)
GPIO.setup(garden_sensor_pin, GPIO.IN)
GPIO.setup(garage_light_pin, GPIO.OUT)
GPIO.setup(garden_light_pin, GPIO.OUT)

def activate_light(sensor_pin, light_pin):
    if GPIO.input(sensor_pin):
        GPIO.output(light_pin, GPIO.HIGH)
    else:
        GPIO.output(light_pin, GPIO.LOW)

try:
    while True:
        activate_light(garage_sensor_pin, garage_light_pin)
        activate_light(garden_sensor_pin, garden_light_pin)
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
