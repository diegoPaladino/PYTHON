import serial
import requests

# Configurações do serial
serial_port = '/dev/ttyUSB0'  # Ajuste conforme a porta serial usada
baud_rate = 9600
timeout = 1

# Configurações da API de SMS
sms_api_url = 'https://api.sms_provider.com/send_sms'
api_key = 'your_api_key'

def send_sms(message):
    """Envia uma mensagem SMS através de uma API."""
    payload = {
        'api_key': api_key,
        'to': 'número_destino',  # Número do telefone de destino
        'message': message
    }
    response = requests.post(sms_api_url, data=payload)
    if response.status_code == 200:
        print("Mensagem enviada com sucesso!")
    else:
        print("Erro ao enviar mensagem.")

def read_pressure():
    """Lê os dados de pressão do pressostato via comunicação serial."""
    with serial.Serial(serial_port, baud_rate, timeout=timeout) as ser:
        if ser.isOpen():
            line = ser.readline().decode('utf-8').strip()
            try:
                pressure = float(line)
                return pressure
            except ValueError:
                print("Erro na leitura dos dados.")
                return None

def monitor_pressure():
    """Monitora a pressão e envia alertas conforme as condições estabelecidas."""
    while True:
        pressure = read_pressure()
        if pressure is not None:
            if 4 <= pressure < 5:
                send_sms("O sistema está no meio da capacidade.")
            elif 0 <= pressure <= 1:
                send_sms("O sistema se encontra vazio.")

if __name__ == '__main__':
    monitor_pressure()
