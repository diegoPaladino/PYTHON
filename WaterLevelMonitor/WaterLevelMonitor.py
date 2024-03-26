#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>

// Substitua pelos seus dados de rede
const char* ssid = "SEU_SSID";
const char* password = "SUA_SENHA";

// Pins dos sensores de nível de água
const int lowLevelPin = D1;
const int midLevelPin = D2;
const int highLevelPin = D3;

// URL do servidor Raspberry Pi (substitua pelo IP correto e porta se necessário)
const String serverUrl = "http://192.168.1.100:5000/update-water-level";

WiFiClient client;

void setup() {
  Serial.begin(115200);
  WiFi.begin(ssid, password);

  pinMode(lowLevelPin, INPUT);
  pinMode(midLevelPin, INPUT);
  pinMode(highLevelPin, INPUT);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("Connected to Wi-Fi");
}

void loop() {
  int lowLevel = digitalRead(lowLevelPin);
  int midLevel = digitalRead(midLevelPin);
  int highLevel = digitalRead(highLevelPin);

  if (WiFi.status() == WL_CONNECTED) {
    HTTPClient http;
    http.begin(client, serverUrl);
    http.addHeader("Content-Type", "application/json");
    String postData = "{\"lowLevel\":" + String(lowLevel) + ",\"midLevel\":" + String(midLevel) + ",\"highLevel\":" + String(highLevel) + "}";
    int httpCode = http.POST(postData);
    String payload = http.getString();
    Serial.println(httpCode);
    Serial.println(payload);
    http.end();
  }
  delay(300000); // Espera 5 minutos antes de enviar os próximos dados
}
