import sounddevice as sd
import numpy as np
import time
from datetime import datetime
import csv
import os

# Configuração inicial
duração_gravação = 10  # Em segundos
frequência_amostral = 44100  # Em Hz
caminho_arquivo = "/home/pi/decibeis_ambiente.csv"  # Ajuste conforme necessário

def medir_decibéis(duração, fs):
    """Grava um áudio por um curto período e calcula os decibéis."""
    gravação = sd.rec(int(duração * fs), samplerate=fs, channels=2, dtype='float64')
    sd.wait()  # Aguarda a gravação terminar
    amplitude = np.sqrt(np.mean(np.square(gravação, axis=0)))
    decibéis = 20 * np.log10(amplitude)
    return np.max(decibéis)

def salvar_dados(timestamp, decibéis):
    """Salva os dados de decibéis com timestamp em um arquivo CSV."""
    cabeçalho = ['Timestamp', 'Decibéis']
    arquivo_existe = os.path.isfile(caminho_arquivo)
    with open(caminho_arquivo, 'a', newline='') as arquivo:
        escritor = csv.writer(arquivo)
        if not arquivo_existe:
            escritor.writerow(cabeçalho)
        escritor.writerow([timestamp, decibéis])

# Loop principal
while True:
    timestamp_atual = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    decibéis = medir_decibéis(duração_gravação, frequência_amostral)
    print(f"{timestamp_atual} - Decibéis: {decibéis:.2f} dB")
    salvar_dados(timestamp_atual, decibéis)
    time.sleep(10)  # Aguarda 10 segundos antes da próxima medição
