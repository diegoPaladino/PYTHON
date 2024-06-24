#include <Arduino.h>
#include <RCSwitch.h>

const int switchPin = 2;           // Pin connected to the switch (Normally Closed)
const int relayPin = 3;            // Pin connected to the relay
const int lightSensorPin = A0;     // Pin connected to the light sensor
const int lightThreshold = 500;    // Threshold for detecting low light (night)
const int countdownTime = 120000;  // Countdown time in milliseconds (2 minutes)

RCSwitch mySwitch = RCSwitch();

void setup() {
    pinMode(switchPin, INPUT_PULLUP);
    pinMode(relayPin, OUTPUT);
    pinMode(lightSensorPin, INPUT);
    mySwitch.enableTransmit(10);  // Pin connected to the RF transmitter
    Serial.begin(9600);
}

void loop() {
    if (digitalRead(switchPin) == LOW) {
        int lightLevel = analogRead(lightSensorPin);
        if (lightLevel < lightThreshold) {
            digitalWrite(relayPin, HIGH);  // Turn on the relay
        } else {
            delay(countdownTime);  // Wait for 2 minutes

            if (digitalRead(switchPin) == HIGH) {
                sendControlSignal();
            }
        }
    }
    digitalWrite(relayPin, LOW);  // Turn off the relay
}

void sendControlSignal() {
    mySwitch.send("3256-14-7522");  // Send the copied control signal
    Serial.println("Control signal sent.");
}
