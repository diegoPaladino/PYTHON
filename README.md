# AmbientTempMonitor

## Introdução
Este projeto consiste em um script Python simples para monitorar a temperatura e a umidade do ambiente utilizando o sensor DHT11.

## Materiais Necessários
- Raspberry Pi (Qualquer modelo com GPIO)
- Sensor de temperatura e umidade DHT11
- Resistência de 10k (opcional, dependendo da configuração)

## Propósito do Projeto
Monitorar as condições ambientais em tempo real, útil para ambientes que necessitam manter parâmetros climáticos específicos.

## Prós e Contras

### Prós
- Fácil de configurar e utilizar
- Baixo custo de implementação
- Utiliza componentes amplamente disponíveis

### Contras
- Precisão limitada do sensor DHT11
- Dependente de hardware específico

## Instruções Gerais
1. Conecte o sensor DHT11 ao Raspberry Pi conforme orientação do fabricante.
2. Instale a biblioteca Adafruit_DHT com `pip install Adafruit_DHT`.
3. Execute o script `ambient_temp_monitor.py` para iniciar o monitoramento.

## Licença
Este projeto é distribuído sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.
