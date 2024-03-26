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
