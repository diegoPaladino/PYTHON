import tkinter as tk
from tkinter import messagebox
import random

class LuckyNumberPickerApp:
    def __init__(self, master):
        self.master = master
        master.title("Lucky Number Picker")
        
        self.min_label = tk.Label(master, text="Minimum Number:")
        self.min_label.pack()
        
        self.min_entry = tk.Entry(master)
        self.min_entry.pack()
        
        self.max_label = tk.Label(master, text="Maximum Number:")
        self.max_label.pack()
        
        self.max_entry = tk.Entry(master)
        self.max_entry.pack()
        
        self.pick_button = tk.Button(master, text="Pick a Lucky Number", command=self.pick_lucky_number)
        self.pick_button.pack()
        
        self.result_label = tk.Label(master, text="", font=("Helvetica", 24))
        self.result_label.pack()
        
    def pick_lucky_number(self):
        try:
            min_number = int(self.min_entry.get())
            max_number = int(self.max_entry.get())
            if min_number > max_number:
                raise ValueError("Minimum number must be less than or equal to maximum number.")
            lucky_number = random.randint(min_number, max_number)
            self.result_label.config(text=f"Your Lucky Number is: {lucky_number}")
        except ValueError as e:
            messagebox.showerror("Invalid input", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = LuckyNumberPickerApp(root)
    root.mainloop()
