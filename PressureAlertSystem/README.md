# PressureAlertSystem

## Introdução
O PressureAlertSystem é uma aplicação Python projetada para monitorar os níveis de pressão via um pressostato conectado a um microcontrolador com módulo GSM. Quando a pressão atinge 4 kgf/cm², um SMS é enviado indicando que o sistema está na metade de sua capacidade. Um segundo alerta é enviado quando a pressão cai para entre 0 e 1 kgf/cm², indicando que o sistema está vazio.

## Materiais Necessários
- Microcontrolador com capacidade de comunicação serial (ex: Arduino, Raspberry Pi)
- Módulo GSM (ex: SIM800L)
- Pressostato com saída adequada para conexão ao microcontrolador

## Propósito do Projeto
Este projeto visa oferecer uma solução de baixo custo e eficiente para monitoramento de pressão em sistemas críticos, onde o conhecimento da capacidade do sistema em tempo real é crucial para a manutenção e segurança operacional.

## Prós e Contras
### Prós
- Comunicação eficiente utilizando SMS para alertas críticos.
- Baixo custo de implementação e manutenção.

### Contras
- Depende da cobertura e da qualidade do serviço da operadora móvel.
- Necessidade de calibração precisa do pressostato para evitar falsos positivos ou negativos.

## Instruções de Instalação
1. Instale Python e as bibliotecas `pyserial` e `requests`.
2. Conecte o módulo GSM e o pressostato ao microcontrolador conforme o diagrama de circuito.
3. Carregue o código fornecido no microcontrolador.
4. Configure o número de destino para os alertas SMS no script Python.

## Licença
Este projeto é disponibilizado sob a Licença MIT.

