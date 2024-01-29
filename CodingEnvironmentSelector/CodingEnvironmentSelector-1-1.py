import tkinter as tk
import subprocess
import time
import pygetwindow as gw
import pyautogui

def maximize_window(title):
    # Espera um pouco para garantir que a janela tenha tempo de abrir
    time.sleep(6)

    # Tenta obter e maximizar a janela
    try:
        window = gw.getWindowsWithTitle(title)[0]
        window.maximize()
    except IndexError:
        print(f"Não foi possível encontrar a janela: {title}")

def open_arduino():
    arduino_exe = "C:\\Program Files (x86)\\Arduino\\arduino.exe"
    arduino_file = "C:\\Users\\diego\\Desktop\\001-Desktop\\diegoPaladino\\Automacao\\ARDUINO\\prompt_chatGPT.txt"
    subprocess.Popen([arduino_exe])
    os.startfile(arduino_file)
    maximize_window("Arduino")

def open_python():
    vscode_exe = "C:\\Users\\diego\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
    python_file = "C:\\Users\\diego\\Desktop\\001-Desktop\\diegoPaladino\\Automação\\PYTHON.txt"
    subprocess.Popen([vscode_exe])
    os.startfile(python_file)
    maximize_window("Visual Studio Code")

def main():
    root = tk.Tk()
    root.title("Escolha o Ambiente")

    btn_arduino = tk.Button(root, text="Arduino", command=open_arduino)
    btn_arduino.pack(pady=10)

    btn_python = tk.Button(root, text="Python", command=open_python)
    btn_python.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
