Para criar um programa que use 3 módulos bóia (sensores de nível de água) para Arduino/Raspberry, configurados para detectar níveis baixo, médio e alto de água em uma caixa d'água e que comunique esses dados através de um NodeMCU conectado a uma rede Wi-Fi, integrando essas informações a um Raspberry Pi que coleta e processa os dados, seguiremos alguns passos essenciais. Abordarei o projeto em duas partes principais: o código para o NodeMCU e uma sugestão de como manipular os dados no Raspberry Pi.

### Nome do Projeto: WaterLevelMonitor

### Parte 1: Código para NodeMCU (ESP8266)

Este código é escrito em C++ para o Arduino IDE, visando o NodeMCU. Ele lê os estados dos sensores de nível de água conectados e envia os dados via Wi-Fi.

```cpp
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
```

### Parte 2: Manipulação de Dados no Raspberry Pi

No Raspberry Pi, você pode usar Python com Flask para criar um servidor web simples que receba os dados do NodeMCU. Instale Flask usando pip:

```
pip install Flask
```

Crie um arquivo `app.py`:

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/update-water-level', methods=['POST'])
def update_water_level():
    data = request.json
    print("Nível Baixo: {}, Nível Médio: {}, Nível Alto: {}".format(data['lowLevel'], data['midLevel'], data['highLevel']))
    # Aqui você pode adicionar o código para processar e armazenar os dados
    return jsonify({"status": "success"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

Execute o servidor com:

```
python app.py
```

Este setup cria um sistema onde o NodeMCU lê os níveis de água e envia esses dados ao Raspberry Pi via Wi-Fi a cada 5 minutos. No Raspberry Pi, o servidor Flask recebe esses dados e você pode expandir o código para salvar em um banco de dados, enviar alertas, etc.

### Título do Commit: 
Adicionado sistema de monitoramento de nível de água

### Descrição do Commit:
Implementação de um sistema que usa NodeMCU para ler 3 sensores de nível de água (baixo, médio, alto) e enviar esses dados para um Raspberry Pi via Wi-Fi. O Raspberry Pi processa e exibe os dados.

### README.md

```
# WaterLevelMonitor

## Introdução
Este projeto utiliza 3 módulos bóia para monitorar o nível de água em uma caixa d'água, enviando os dados para um Raspberry Pi através de um NodeMCU.

## Materiais Necessários
- 1 x NodeMCU ESP8266
- 3 x Módulos bóia (sensores de nível de água)
- 1 x Raspberry Pi
- Cabos de conexão

## Propósito do Projeto
Monitorar os níveis de água em uma caixa d'água e fornecer uma interface de visualização dos dados.

## Prós e Contras
**Prós:**
- Monitoramento em tempo real
- Fácil instalação

**Contras:**
- Necessita de conexão Wi-Fi estável
- Limitado aos pontos fixos de medição (baixo, médio, alto)

## Instruções Gerais
1. Conecte os sensores ao NodeMCU conforme o código.
2. Carregue o código no NodeMCU.
3. Configure o Raspberry Pi para rodar o servidor Flask.
4. Verifique os dados recebidos através do Flask.

## Licença
MIT
```

### Ícone Isométrico

Para completar, vou criar um ícone isométrico minimalista que representa o projeto de monitoramento de nível de água com Python e hardware.

```json
{
  "prompt": "A minimalist, isometric icon representing a water level monitoring project using Python and Arduino/Raspberry Pi hardware. The icon should include symbols or elements indicating water, sensors, and Wi-Fi connectivity, all in a clean, technical, and modern style. The color scheme should include shades of blue, white, and black to convey the theme of water and technology."
}
```

Aqui está o ícone isométrico minimalista que representa o projeto de monitoramento de nível de água usando Python e hardware Arduino/Raspberry Pi. Este ícone combina elementos que simbolizam água, sensores e conectividade Wi-Fi em um estilo limpo, técnico e moderno, seguindo a paleta de cores sugerida.