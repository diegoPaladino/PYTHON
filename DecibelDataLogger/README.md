# DecibelDataLogger

## Introdução
Este programa foi desenvolvido para o Raspberry Pi Pico Model 2B, com o objetivo de registrar os níveis de decibéis utilizando o módulo microfone KY-037. Os dados são monitorados continuamente, registrando o máximo, mínimo e a média de decibéis a cada minuto em um arquivo CSV.

## Materiais Necessários
- Raspberry Pi Pico Model 2B
- MicroPython instalado no Raspberry Pi Pico
- Módulo microfone KY-037
- Cabos de conexão

## Propósito do Projeto
Monitorar os níveis de ruído em um ambiente por um período prolongado, permitindo análises detalhadas dos padrões de ruído.

## Prós e Contras
**Prós:**
- Monitoramento contínuo e automático de decibéis.
- Geração de dados em formato CSV para fácil análise.

**Contras:**
- Necessidade de calibração do microfone para precisão dos dados.
- Limitado pela capacidade de armazenamento do dispositivo.

## Diretrizes Gerais
1. Conecte corretamente o módulo microfone KY-037 ao Raspberry Pi Pico.
2. Carregue o código fornecido no Raspberry Pi Pico.
3. O arquivo `dados_decibeis.csv` será atualizado continuamente enquanto o programa estiver em execução.

## Licença
MIT License
