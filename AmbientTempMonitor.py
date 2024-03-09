import Adafruit_DHT
import time

# Definição do tipo de sensor
SENSOR = Adafruit_DHT.DHT11

# Defina o pino GPIO ao qual o sensor está conectado
GPIO_PIN = 4

def read_sensor():
    """Lê a umidade e a temperatura do sensor DHT11."""
    humidity, temperature = Adafruit_DHT.read(SENSOR, GPIO_PIN)
    if humidity is not None and temperature is not None:
        print(f"Temperatura: {temperature}°C  Umidade: {humidity}%")
    else:
        print("Falha ao ler do sensor. Tente novamente.")

if __name__ == "__main__":
    print("Monitoramento da temperatura do ambiente iniciado.")
    try:
        while True:
            read_sensor()
            time.sleep(2)  # Aguarda 2 segundos antes da próxima leitura
    except KeyboardInterrupt:
        print("Monitoramento encerrado.")
