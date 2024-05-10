#this principle is based in Kaisser's knowledge 


import tkinter as tk

def update_buttons(button_clicked):
    for button in buttons:
        if button != button_clicked and button_clicked["state"] == "normal":
            button["state"] = "disabled"
        elif button == button_clicked and button_clicked["state"] == "disabled":
            button["state"] = "normal"

# Cria a janela principal
root = tk.Tk()
root.title("TriButtonSelector")

# Lista de botões
buttons = []

# Função que será chamada quando um botão for pressionado
def on_button_click(button):
    update_buttons(button)

# Cria os botões e os adiciona à lista
for text in ["BOM", "BONITO", "BARATO", "RAPIDO"]:
    button = tk.Button(root, text=text, width=10, height=2, command=lambda b=button: on_button_click(b))
    button.pack(pady=5)
    buttons.append(button)

# Inicia o loop da aplicação
root.mainloop()
