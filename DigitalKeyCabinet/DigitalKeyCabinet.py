import RPi.GPIO as GPIO
import time
from Adafruit_CharLCD import Adafruit_CharLCD
import sqlite3
from datetime import datetime

# Configuração inicial do LCD via I2C
lcd = Adafruit_CharLCD(rs=1, en=2, d4=3, d5=4, d6=5, d7=6, cols=24, lines=2)
lcd.begin(24, 2)

# Configuração do teclado numérico
MATRIX = [['1', '2', '3'],
          ['4', '5', '6'],
          ['7', '8', '9'],
          ['*', '0', '#']]
ROW_PINS = [7, 8, 9, 10]  # altere de acordo com suas conexões
COL_PINS = [11, 12, 13]  # altere de acordo com suas conexões

GPIO.setmode(GPIO.BOARD)

for j in range(3):
    GPIO.setup(COL_PINS[j], GPIO.OUT)
    GPIO.output(COL_PINS[j], 1)

for i in range(4):
    GPIO.setup(ROW_PINS[i], GPIO.IN, pull_up_down=GPIO.PUD_UP)

def keypress():
    try:
        while True:
            for j in range(3):
                GPIO.output(COL_PINS[j], 0)
                for i in range(4):
                    if GPIO.input(ROW_PINS[i]) == 0:
                        return MATRIX[i][j]
                GPIO.output(COL_PINS[j], 1)
    finally:
        GPIO.cleanup()

# Função para inicializar o banco de dados
def init_db():
    conn = sqlite3.connect('keycabinet.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS keys
                 (timestamp TEXT, user_id TEXT, action TEXT)''')
    conn.commit()
    conn.close()

# Função para registrar a ação no banco de dados
def log_key_action(user_id, action):
    conn = sqlite3.connect('keycabinet.db')
    c = conn.cursor()
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    c.execute("INSERT INTO keys VALUES (?, ?, ?)", (now, user_id, action))
    conn.commit()
    conn.close()

init_db()

# Loop principal
while True:
    lcd.clear()
    lcd.message('Insira seu ID:')
    user_id = ''
    while True:
        key = keypress()
        if key == '#':
            log_key_action(user_id, 'RETRIEVE' if action == '1' else 'RETURN')
            lcd.clear()
            lcd.message('Chave ' + ('retirada' if action == '1' else 'reposta'))
            time.sleep(2)
            break
        elif key == '*':
            user_id = ''
            lcd.clear()
            lcd.message('ID cancelado\nInsira novamente:')
        else:
            user_id += key
            lcd.clear()
            lcd.message(f'ID: {user_id}\n# Concluir, * Cancelar')
