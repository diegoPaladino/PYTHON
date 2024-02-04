import datetime
import sounddevice as sd
import numpy as np
import pandas as pd
import time

def record_decibels(duration=60, interval=10, filename='decibel_log.csv'):
    start_time = time.time()
    next_record_time = start_time + interval
    data = []

    def audio_callback(indata, frames, time, status):
        if status:
            print(status)
        current_time = datetime.datetime.now()
        if current_time.timestamp() >= next_record_time:
            volume_norm = np.linalg.norm(indata) * 10
            decibels = 20 * np.log10(volume_norm)
            data.append([current_time.strftime("%Y-%m-%d %H:%M:%S"), decibels])
            next_record_time += interval

    with sd.InputStream(callback=audio_callback):
        while time.time() - start_time < duration:
            sd.sleep(interval * 1000 - (time.time() - start_time) % (interval * 1000))

    df = pd.DataFrame(data, columns=['Timestamp', 'Decibels'])
    df.to_csv(filename, index=False)

# Ajuste conforme necessário para gravar por um período específico ou até que uma condição seja atendida
