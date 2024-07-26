#necessary item: card 8Gb


from machine import Pin, ADC
import utime
import uos

#to OS is necessary 8Gb SD card

# Configuração do ADC para leitura do microfone
adc = ADC(Pin(26)) # Altere o número do pino conforme sua conexão

# Função para ler e calcular os decibéis
def ler_decibeis():
    max_decibel = 0
    min_decibel = 1023  # Valor máximo para um ADC de 10 bits
    soma_decibeis = 0
    leituras = 0

    inicio = utime.ticks_ms()
    
    while utime.ticks_diff(utime.ticks_ms(), inicio) < 60000:  # 60 segundos
        valor = adc.read_u16()
        decibel = valor / 65535 * 1023  # Conversão para escala de 10 bits (0-1023)
        max_decibel = max(max_decibel, decibel)
        min_decibel = min(min_decibel, decibel)
        soma_decibeis += decibel
        leituras += 1
        utime.sleep(0.01)  # Pequena pausa para não sobrecarregar o ADC

    media_decibel = soma_decibeis / leituras
    return min_decibel, max_decibel, media_decibel

# Preparação do arquivo CSV
nome_arquivo = "dados_decibeis.csv"
with open(nome_arquivo, "w") as arquivo:
    arquivo.write("Minimo,Maximo,Media\n")

# Loop principal
try:
    while True:
        minimo, maximo, media = ler_decibeis()
        with open(nome_arquivo, "a") as arquivo:
            arquivo.write(f"{minimo},{maximo},{media}\n")
        print(f"Min: {minimo}, Max: {maximo}, Media: {media}")
except KeyboardInterrupt:
    print("Programa encerrado.")
    
    
#implementate in the school to know the ambience health