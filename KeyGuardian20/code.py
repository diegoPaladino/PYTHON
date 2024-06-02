import I2C_LCD_driver
from time import sleep

# Configuração inicial do display LCD
mylcd = I2C_LCD_driver.lcd()

# Dicionário para armazenar usuários e senhas
usuarios = {
    "DIEGO": "1234",
    "MARIA": "5678",
    "JOAO": "91011",
    "BETO": "1213"
}

def adicionar_usuario(nome, senha):
    """Adiciona um novo usuário ao sistema."""
    if nome.upper() in usuarios:
        mylcd.lcd_display_string("Usuario ja existe", 1)
    else:
        usuarios[nome.upper()] = senha
        mylcd.lcd_display_string("Usuario adicionado", 1)
    sleep(2)
    mylcd.lcd_clear()

def remover_usuario(nome):
    """Remove um usuário existente do sistema."""
    if nome.upper() in usuarios:
        del usuarios[nome.upper()]
        mylcd.lcd_display_string("Usuario removido", 1)
    else:
        mylcd.lcd_display_string("Usuario nao encontrado", 1)
    sleep(2)
    mylcd.lcd_clear()

# Exemplo de uso das funções
adicionar_usuario("DIEGO", "1234")
remover_usuario("JOAO")

#entender essas funções 
