from machine import ADC, Pin
import utime

# Configuração do ADC
adc = ADC(Pin(26)) # ADC0 no GPIO26, ajuste conforme a sua conexão

# Constantes
Vcc = 3.3 # Tensão de alimentação do Raspberry Pi Pico

def ler_resistencia():
    valor_adc = adc.read_u16() # Lê o valor do ADC (0-65535)
    tensao = (valor_adc / 65535) * Vcc # Converte para tensão (0-Vcc)
    
    # Supondo que você conhece os valores dos resistores e como eles estão configurados,
    # você pode calcular a resistência baseando-se na tensão medida.
    # Esta é uma simplificação. A fórmula real dependerá da configuração do seu ladder resistor.
    resistencia = tensao # Exemplo simplificado, substitua pela sua fórmula real
    
    return resistencia

while True:
    resistencia = ler_resistencia()
    print(f"Resistência medida: {resistencia:.2f} Ohms")
    utime.sleep(1) # Aguarda 1 segundo antes da próxima leitura
