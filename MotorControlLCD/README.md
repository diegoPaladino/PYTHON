# MotorControlLCD

## Introdução
Este projeto visa fornecer uma maneira simplificada de controlar motores e um display LCD, traduzido e adaptado de Arduino para Python, utilizando um Raspberry Pi.

## Materiais Necessários
- Raspberry Pi (qualquer modelo com GPIO)
- Motores de passo
- Display LCD com interface I2C
- Botões e resistores para debouncing
- LEDs
- Fios e protoboard

## Propósito do Projeto
Facilitar o controle de motores e a interação com um display LCD para projetos de automação ou robótica educacional, oferecendo uma base para expansão e personalização.

### Pros
- Código base em Python facilita a integração com outros sistemas e bibliotecas.
- Estrutura simplificada para fácil compreensão e modificação.

### Contras
- Requer adaptações específicas para diferentes hardwares e configurações.
- Depende da disponibilidade de bibliotecas Python para controle de hardware específico.

## Diretrizes Gerais
1. Clone o repositório para seu Raspberry Pi.
2. Instale as dependências necessárias: `RPi.GPIO`, `SomeI2CLibrary` (nome fictício, substitua pela biblioteca adequada ao seu LCD).
3. Conecte os componentes de hardware conforme esquematizado.
4. Execute o script `motor_control_lcd.py` para iniciar o controle dos motores e LCD.

## Licença
Este projeto é distribuído sob a licença MIT, permitindo a utilização e modificação livre por qualquer pessoa.

