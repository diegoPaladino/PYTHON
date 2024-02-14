import time
import board
import adafruit_dht
from digitalio import DigitalInOut, Direction
from adafruit_lorafi import LoRa, Modulation

# Initialize DHT sensor for temperature and humidity
dht_device = adafruit_dht.DHT22(board.D4)

# Initialize the relay pin
relay_pin = DigitalInOut(board.D5)
relay_pin.direction = Direction.OUTPUT

# LoRa configuration
lora = LoRa(
    modulation=Modulation.LORA,
    frequency=868E6,
    tx_power=14,
    bandwidth=125E3,
    spreading_factor=7,
    coding_rate=5,
    sync_word=0x34,
    implicit_header=False,
    crc=True,
    power_save=True)

def check_and_feed():
    """Check conditions and feed fish if criteria met."""
    try:
        # Read environmental conditions
        temperature = dht_device.temperature
        humidity = dht_device.humidity
        
        # Check if conditions are suitable for feeding
        if 20 <= temperature <= 30:
            print("Feeding time!")
            relay_pin.value = True  # Activate relay to feed fish
            time.sleep(10)  # Feeding duration
            relay_pin.value = False
        else:
            print("Conditions not suitable for feeding.")
            
        # Send data over LoRa
        lora.send(f"Temp: {temperature}, Humidity: {humidity}")
        
    except RuntimeError as error:
        print(f"Reading error: {error}")

def main():
    while True:
        check_and_feed()
        time.sleep(3600)  # Check every hour

if __name__ == "__main__":
    main()
