import tkinter as tk
from tkinter import simpledialog
import subprocess
import os

def open_arduino():
    arduino_exe = "C:\\Program Files (x86)\\Arduino\\arduino.exe"
    arduino_file = "C:\\Users\\diego\\Desktop\\001-Desktop\\diegoPaladino\\Automação\\ARDUINO.txt"
    subprocess.Popen([arduino_exe])
    os.startfile(arduino_file)

def open_python():
    vscode_exe = "C:\\Users\\diego\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
    python_file = "C:\\Users\\diego\\Desktop\\001-Desktop\\diegoPaladino\\Automação\\PYTHON.txt"
    subprocess.Popen([vscode_exe])
    os.startfile(python_file)

def main():
    root = tk.Tk()
    root.withdraw()  # Esconde a janela principal do Tkinter
    choice = simpledialog.askstring("Escolha o Ambiente", "Digite Arduino ou Python:", parent=root)
    
    if choice and choice.lower() == 'arduino':
        open_arduino()
    elif choice and choice.lower() == 'python':
        open_python()
    else:
        print("Escolha inválida. Por favor, digite 'Arduino' ou 'Python'.")

if __name__ == "__main__":
    main()
