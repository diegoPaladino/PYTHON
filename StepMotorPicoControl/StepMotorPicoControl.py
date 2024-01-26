import machine
import utime

# Definição dos pinos para os motores de passo
MOTOR1_STEP_PIN = 2  # Substituir pelo pino correto
MOTOR1_DIR_PIN = 3   # Substituir pelo pino correto
MOTOR2_STEP_PIN = 4  # Substituir pelo pino correto
MOTOR2_DIR_PIN = 5   # Substituir pelo pino correto

# Configuração dos motores
step_pin_motor1 = machine.Pin(MOTOR1_STEP_PIN, machine.Pin.OUT)
dir_pin_motor1 = machine.Pin(MOTOR1_DIR_PIN, machine.Pin.OUT)
step_pin_motor2 = machine.Pin(MOTOR2_STEP_PIN, machine.Pin.OUT)
dir_pin_motor2 = machine.Pin(MOTOR2_DIR_PIN, machine.Pin.OUT)

# Variáveis de configuração
steps_per_mm = 50  # Ajustar conforme o motor e a configuração mecânica
delay = 0.002     # Ajustar conforme a velocidade desejada

def move_motor(step_pin, dir_pin, direction, distance_mm):
    dir_pin.value(direction)
    for _ in range(distance_mm * steps_per_mm):
        step_pin.value(1)
        utime.sleep(delay)
        step_pin.value(0)
        utime.sleep(delay)

# Movendo 100mm em cada direção para cada motor
move_motor(step_pin_motor1, dir_pin_motor1, 1, 100)  # Motor 1, 100mm
utime.sleep(1)
move_motor(step_pin_motor1, dir_pin_motor1, 0, 100)  # Motor 1, -100mm

move_motor(step_pin_motor2, dir_pin_motor2, 1, 100)  # Motor 2, 100mm
utime.sleep(1)
move_motor(step_pin_motor2, dir_pin_motor2, 0, 100)  # Motor 2, -100mm
