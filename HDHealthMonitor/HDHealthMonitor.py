import os
import datetime
import pandas as pd
import psutil

def get_hd_usage(path="/"):
    """Returns the total usage of the given path in gigabytes."""
    usage = psutil.disk_usage(path)
    used_gb = usage.used / (1024 ** 3)  # Convertendo bytes para gigabytes
    return round(used_gb, 2)

def log_hd_usage(log_file="hd_usage_log.csv"):
    """Logs the daily HD usage in a CSV file."""
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    usage_gb = get_hd_usage()
    
    if not os.path.exists(log_file):
        df = pd.DataFrame(columns=["Date", "Usage(GB)"])
    else:
        df = pd.read_csv(log_file)
    
    # Usando pandas.concat em vez de df.append
    new_row = pd.DataFrame({"Date": [today], "Usage(GB)": [usage_gb]})
    df = pd.concat([df, new_row], ignore_index=True)
    
    df.to_csv(log_file, index=False)

log_hd_usage()
