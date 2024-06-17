import RPi.GPIO as GPIO
import time
from datetime import datetime

# Configuração dos pinos GPIO
LIGHT_PIN = 18
SWITCH_PIN = 23
GATE_SENSOR_PIN = 24
LIGHT_SENSOR_PIN = 25

GPIO.setmode(GPIO.BCM)
GPIO.setup(LIGHT_PIN, GPIO.OUT)
GPIO.setup(SWITCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(GATE_SENSOR_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(LIGHT_SENSOR_PIN, GPIO.IN)

def is_night():
    return GPIO.input(LIGHT_SENSOR_PIN) == 0

def gate_opened():
    return GPIO.input(GATE_SENSOR_PIN) == 0

def switch_pressed():
    return GPIO.input(SWITCH_PIN) == 0

def turn_on_light():
    GPIO.output(LIGHT_PIN, GPIO.HIGH)

def turn_off_light():
    GPIO.output(LIGHT_PIN, GPIO.LOW)

try:
    while True:
        if is_night() and gate_opened():
            turn_on_light()
            time.sleep(5 * 60)  # Mantém a luz acesa por 5 minutos
            turn_off_light()
        
        if switch_pressed():
            if GPIO.input(LIGHT_PIN) == GPIO.LOW:
                turn_on_light()
            else:
                turn_off_light()
        
        time.sleep(0.1)

except KeyboardInterrupt:
    GPIO.cleanup()
