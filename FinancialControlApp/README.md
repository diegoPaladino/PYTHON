import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt

class FinancialControlApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Financial Control App")
        
        self.entries = []
        self.labels = []
        
        self.setup_ui()
    
    def setup_ui(self):
        self.add_entry()
        
        add_button = tk.Button(self.root, text="Add Expense", command=self.add_entry)
        add_button.pack(pady=10)
        
        graph_button = tk.Button(self.root, text="Generate Graph", command=self.generate_graph)
        graph_button.pack(pady=10)
        
    def add_entry(self):
        frame = tk.Frame(self.root)
        frame.pack(pady=5)
        
        label = tk.Label(frame, text="Expense Description:")
        label.pack(side=tk.LEFT)
        
        entry_desc = tk.Entry(frame)
        entry_desc.pack(side=tk.LEFT, padx=5)
        
        label = tk.Label(frame, text="Amount:")
        label.pack(side=tk.LEFT)
        
        entry_amount = tk.Entry(frame)
        entry_amount.pack(side=tk.LEFT, padx=5)
        
        self.entries.append((entry_desc, entry_amount))
    
    def generate_graph(self):
        descriptions = []
        amounts = []
        
        for desc_entry, amount_entry in self.entries:
            desc = desc_entry.get()
            try:
                amount = float(amount_entry.get())
            except ValueError:
                messagebox.showerror("Input Error", "Please enter a valid number for the amount.")
                return
            
            descriptions.append(desc)
            amounts.append(amount)
        
        if not descriptions:
            messagebox.showinfo("No Data", "No expenses to show.")
            return
        
        plt.figure(figsize=(10, 5))
        plt.bar(descriptions, amounts, color='blue')
        plt.xlabel('Expenses')
        plt.ylabel('Amount')
        plt.title('Expense Distribution')
        plt.show()

if __name__ == "__main__":
    root = tk.Tk()
    app = FinancialControlApp(root)
    root.mainloop()
