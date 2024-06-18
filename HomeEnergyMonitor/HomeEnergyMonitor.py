import paho.mqtt.client as mqtt
import sqlite3
from datetime import datetime

# MQTT settings
MQTT_BROKER = "mqtt.example.com"
MQTT_PORT = 1883
MQTT_TOPIC = "home/energy"

# Database settings
DB_NAME = "energy_data.db"

# Database setup
def setup_database():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS energy_consumption (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        timestamp TEXT,
                        point TEXT,
                        amperage REAL)''')
    conn.commit()
    conn.close()

# MQTT callback for receiving messages
def on_message(client, userdata, message):
    data = message.payload.decode('utf-8')
    point, amperage = data.split(',')
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    save_data(timestamp, point, float(amperage))

# Save data to the database
def save_data(timestamp, point, amperage):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO energy_consumption (timestamp, point, amperage) VALUES (?, ?, ?)", 
                   (timestamp, point, amperage))
    conn.commit()
    conn.close()

# MQTT setup
client = mqtt.Client()
client.on_message = on_message
client.connect(MQTT_BROKER, MQTT_PORT, 60)
client.subscribe(MQTT_TOPIC)
client.loop_start()

# Setup database
setup_database()

# Keep the script running
try:
    while True:
        pass
except KeyboardInterrupt:
    client.loop_stop()
    client.disconnect()
