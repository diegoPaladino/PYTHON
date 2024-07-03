import tkinter as tk
from tkinter import messagebox, simpledialog
import json

class InventoryManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Inventory Management System")
        
        self.inventory = {}
        self.load_inventory()
        
        self.setup_ui()
    
    def setup_ui(self):
        self.listbox = tk.Listbox(self.root, width=50, height=15)
        self.listbox.pack(pady=10)
        
        add_button = tk.Button(self.root, text="Add Item", command=self.add_item)
        add_button.pack(pady=5)
        
        update_button = tk.Button(self.root, text="Update Item", command=self.update_item)
        update_button.pack(pady=5)
        
        view_button = tk.Button(self.root, text="View Inventory", command=self.view_inventory)
        view_button.pack(pady=5)
    
    def add_item(self):
        name = simpledialog.askstring("Input", "Enter item name:")
        if not name:
            return
        quantity = simpledialog.askinteger("Input", "Enter item quantity:")
        if quantity is None:
            return
        
        self.inventory[name] = self.inventory.get(name, 0) + quantity
        self.save_inventory()
        messagebox.showinfo("Success", f"Added {quantity} of {name} to inventory.")
    
    def update_item(self):
        name = simpledialog.askstring("Input", "Enter item name to update:")
        if not name:
            return
        if name not in self.inventory:
            messagebox.showerror("Error", "Item not found in inventory.")
            return
        
        quantity = simpledialog.askinteger("Input", "Enter new item quantity:")
        if quantity is None:
            return
        
        self.inventory[name] = quantity
        self.save_inventory()
        messagebox.showinfo("Success", f"Updated {name} quantity to {quantity}.")
    
    def view_inventory(self):
        self.listbox.delete(0, tk.END)
        for name, quantity in self.inventory.items():
            self.listbox.insert(tk.END, f"{name}: {quantity}")
    
    def save_inventory(self):
        with open('inventory.json', 'w') as file:
            json.dump(self.inventory, file)
    
    def load_inventory(self):
        try:
            with open('inventory.json', 'r') as file:
                self.inventory = json.load(file)
        except FileNotFoundError:
            self.inventory = {}

if __name__ == "__main__":
    root = tk.Tk()
    app = InventoryManagementSystem(root)
    root.mainloop()
