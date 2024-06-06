import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

class RFIDAccessControl:
    def __init__(self, relay_pin):
        self.relay_pin = relay_pin
        self.reader = SimpleMFRC522()
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.relay_pin, GPIO.OUT)
        GPIO.output(self.relay_pin, GPIO.LOW)

    def read_rfid(self):
        try:
            id, text = self.reader.read()
            return id
        except Exception as e:
            print(f"Error reading RFID: {e}")
            return None

    def grant_access(self):
        GPIO.output(self.relay_pin, GPIO.HIGH)
        print("Access Granted")
        GPIO.output(self.relay_pin, GPIO.LOW)

    def deny_access(self):
        print("Access Denied")

    def cleanup(self):
        GPIO.cleanup()

    def run(self, valid_ids):
        try:
            print("Hold a tag near the reader")
            while True:
                rfid_id = self.read_rfid()
                if rfid_id:
                    if rfid_id in valid_ids:
                        self.grant_access()
                    else:
                        self.deny_access()
        finally:
            self.cleanup()

if __name__ == "__main__":
    valid_rfid_ids = [123456789, 987654321]  # Example valid RFID IDs
    access_control = RFIDAccessControl(relay_pin=17)
    access_control.run(valid_ids=valid_rfid_ids)
