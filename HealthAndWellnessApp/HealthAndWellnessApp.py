import tkinter as tk
from tkinter import simpledialog, messagebox
import json

class HealthAndWellnessApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Health and Wellness App")
        
        self.activities = []
        self.load_activities()
        
        self.setup_ui()
    
    def setup_ui(self):
        self.listbox = tk.Listbox(self.root, width=50, height=15)
        self.listbox.pack(pady=10)
        
        add_button = tk.Button(self.root, text="Add Activity", command=self.add_activity)
        add_button.pack(pady=5)
        
        summary_button = tk.Button(self.root, text="View Summary", command=self.view_summary)
        summary_button.pack(pady=5)
        
        tips_button = tk.Button(self.root, text="Health Tips", command=self.show_tips)
        tips_button.pack(pady=5)
    
    def add_activity(self):
        activity = simpledialog.askstring("Input", "Enter activity (e.g., running, yoga):")
        if not activity:
            return
        duration = simpledialog.askinteger("Input", "Enter duration in minutes:")
        if duration is None:
            return
        
        self.activities.append((activity, duration))
        self.save_activities()
        messagebox.showinfo("Success", f"Added activity: {activity} for {duration} minutes.")
    
    def view_summary(self):
        self.listbox.delete(0, tk.END)
        total_duration = 0
        for activity, duration in self.activities:
            self.listbox.insert(tk.END, f"{activity}: {duration} minutes")
            total_duration += duration
        
        self.listbox.insert(tk.END, f"\nTotal duration: {total_duration} minutes")
    
    def show_tips(self):
        tips = [
            "Stay hydrated by drinking at least 8 cups of water a day.",
            "Get at least 30 minutes of exercise daily.",
            "Eat a balanced diet rich in fruits and vegetables.",
            "Take regular breaks to avoid burnout.",
            "Get 7-8 hours of sleep each night."
        ]
        tip = tips[len(self.activities) % len(tips)]
        messagebox.showinfo("Health Tip", tip)
    
    def save_activities(self):
        with open('activities.json', 'w') as file:
            json.dump(self.activities, file)
    
    def load_activities(self):
        try:
            with open('activities.json', 'r') as file:
                self.activities = json.load(file)
        except FileNotFoundError:
            self.activities = []

if __name__ == "__main__":
    root = tk.Tk()
    app = HealthAndWellnessApp(root)
    root.mainloop()
