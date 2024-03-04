# SoundLevelMonitor

## Introdução
Este projeto oferece uma solução para monitoramento contínuo dos níveis de decibéis ambiente utilizando um Raspberry Pi Model 2B. Os dados são medidos a cada 10 segundos e armazenados em um arquivo CSV no SDCard do dispositivo.

## Instalação
Para executar este script, é necessário instalar as bibliotecas `sounddevice` e `numpy`. Isso pode ser feito através do comando `pip install sounddevice numpy`.

## Materiais Necessários
- Raspberry Pi Model 2B
- Microfone compatível com Raspberry Pi
- Cartão SD com Raspbian OS instalado

## Propósito do Projeto
O objetivo deste projeto é fornecer uma ferramenta simples para o monitoramento dos níveis de ruído ambiente, útil em diversas aplicações como estudos ambientais, controle de ruído em escritórios ou fábricas, entre outros.

## Prós e Contras
### Prós
- Fácil de configurar e usar
- Baixo custo de implementação

### Contras
- Depende da precisão do microfone utilizado
- Armazenamento limitado pelo tamanho do SDCard

## Diretrizes Gerais
- Certifique-se de que o microfone esteja corretamente conectado e configurado no Raspberry Pi antes de iniciar o programa.
- Ajuste o caminho do arquivo CSV conforme necessário para corresponder ao seu ambiente de armazenamento.

## Licença
Este projeto é distribuído sob a licença MIT.
