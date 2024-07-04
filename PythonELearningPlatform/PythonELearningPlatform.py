import tkinter as tk
from tkinter import simpledialog, messagebox

class PythonELearningPlatform:
    def __init__(self, root):
        self.root = root
        self.root.title("Python E-Learning Platform")
        
        self.courses = {}
        
        self.setup_ui()
    
    def setup_ui(self):
        self.listbox = tk.Listbox(self.root, width=50, height=15)
        self.listbox.pack(pady=10)
        
        add_button = tk.Button(self.root, text="Add Course", command=self.add_course)
        add_button.pack(pady=5)
        
        view_button = tk.Button(self.root, text="View Courses", command=self.view_courses)
        view_button.pack(pady=5)
        
        access_button = tk.Button(self.root, text="Access Course", command=self.access_course)
        access_button.pack(pady=5)
    
    def add_course(self):
        course_name = simpledialog.askstring("Input", "Enter course name:")
        if not course_name:
            return
        course_content = simpledialog.askstring("Input", "Enter course content:")
        if not course_content:
            return
        
        self.courses[course_name] = course_content
        messagebox.showinfo("Success", f"Course '{course_name}' added.")
    
    def view_courses(self):
        self.listbox.delete(0, tk.END)
        for course_name in self.courses.keys():
            self.listbox.insert(tk.END, course_name)
    
    def access_course(self):
        selected_course = self.listbox.get(tk.ACTIVE)
        if not selected_course:
            messagebox.showerror("Error", "No course selected.")
            return
        
        course_content = self.courses[selected_course]
        messagebox.showinfo("Course Content", f"Content of {selected_course}:\n\n{course_content}")

if __name__ == "__main__":
    root = tk.Tk()
    app = PythonELearningPlatform(root)
    root.mainloop()
