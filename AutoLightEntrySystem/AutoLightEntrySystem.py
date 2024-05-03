#comments about the project:
# serial with the gate motor?



from gpiozero import LightSensor, MotionSensor, Button, OutputDevice
from time import sleep

# Definição dos pinos GPIO para os componentes
PIN_LUZ = 18  # Pino conectado ao relé
PIN_LDR = 17  # Pino conectado ao sensor de luz
PIN_PIR = 27  # Pino conectado ao sensor de movimento
PIN_SWITCH = 22  # Pino conectado ao switch manual

# Inicialização dos sensores e dispositivos
ldr = LightSensor(PIN_LDR)
pir = MotionSensor(PIN_PIR)
switch = Button(PIN_SWITCH)
luz = OutputDevice(PIN_LUZ)

def acender_luzes():
    """Acende as luzes controladas pelo relé."""
    luz.on()
    print("Luzes acesas")

def apagar_luzes():
    """Apaga as luzes controladas pelo relé."""
    luz.off()
    print("Luzes apagadas")

# Loop principal do programa
try:
    while True:
        # Verifica condições para acender as luzes
        if ldr.value > 0.5 and (pir.motion_detected or switch.is_pressed):
            acender_luzes()
        else:
            apagar_luzes()
        sleep(0.5)
except KeyboardInterrupt:
    pass
finally:
    apagar_luzes()  # Garante que as luzes sejam apagadas ao terminar
