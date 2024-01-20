# FaceLockWorkstation

## Introdução
FaceLockWorkstation é um projeto Python que usa reconhecimento facial para aumentar a segurança do seu computador. Quando um rosto não autorizado é detectado, ele automaticamente cria uma nova área de trabalho no Windows para proteger suas informações.

## Lista de Materiais Necessários
- Python 3.x
- OpenCV (`opencv-python-headless`)
- PyAutoGUI

## Propósito do Projeto
Este projeto foi criado para oferecer uma camada adicional de segurança para usuários que deixam seus computadores sem supervisão. Ele é útil em ambientes de trabalho ou espaços compartilhados.

## Prós e Contras
**Prós:**
- Aumenta a segurança do computador.
- Automático e fácil de usar.

**Contras:**
- Requer a webcam sempre ligada.
- Pode haver falsos positivos em ambientes movimentados.

## Orientações Gerais
Para usar este projeto:
1. Instale as dependências: `pip install opencv-python-headless pyautogui`.
2. Execute o script: `python FaceLockWorkstation.py`.
3. Para interromper, pressione 'q' na janela da webcam.

## Licença
Este projeto é open-source e está disponível gratuitamente para uso sob a licença MIT.
