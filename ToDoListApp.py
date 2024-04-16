import tkinter as tk
from tkinter import messagebox
import pickle as pk

# Function to add tasks
def add_task():
    task = entry_task.get()
    if task:
        list_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning('Alert', 'You have not written any task.')

# Function to delete tasks
def delete_task():
    try:
        index = list_tasks.curselection()[0]
        list_tasks.delete(index)
    except IndexError:
        messagebox.showerror("Error", "No task selected.")

# Function to save tasks
def save_tasks():
    tasks = list_tasks.get(0, tk.END)
    with open("to_do_tasks.pkl", "wb") as file:
        pk.dump(tasks, file)

# Function to load tasks
def load_tasks():
    try:
        with open("to_do_tasks.pkl", "rb") as file:
            tasks = pk.load(file)
            list_tasks.delete(0, tk.END)
            for task in tasks:
                list_tasks.insert(tk.END, task)
    except FileNotFoundError:
        messagebox.showerror("Error", "No tasks saved yet.")

# Create the main window
window = tk.Tk()
window.title("To-Do List Application")
window.geometry("700x500")
window.configure(bg="#f0f0f0")

# Heading Label
heading_label = tk.Label(window, text="The To-Do List", font=("Helvetica", 30, "bold"), bg="#2c3e50", fg="#ffffff", padx=10, pady=10)
heading_label.pack(fill=tk.X)

# Entry for adding tasks
entry_task = tk.Entry(window, width=40, font=("Arial", 12))
entry_task.pack(pady=10)

# Listbox to display tasks
list_tasks = tk.Listbox(window, width=60, height=15, font=("Arial", 12))
list_tasks.pack(pady=10)

# Buttons
button_frame = tk.Frame(window, bg="#f0f0f0")
button_frame.pack()

add_button = tk.Button(button_frame, text="Add Task", font=("Arial", 12), bg="#27ae60", fg="#ffffff", padx=10, pady=5, command=add_task)
add_button.grid(row=0, column=0, padx=10)

remove_button = tk.Button(button_frame, text="Remove Task", font=("Arial", 12), bg="#c0392b", fg="#ffffff", padx=10, pady=5, command=delete_task)
remove_button.grid(row=0, column=1, padx=10)

save_button = tk.Button(button_frame, text="Save Tasks", font=("Arial", 12), bg="#2980b9", fg="#ffffff", padx=10, pady=5, command=save_tasks)
save_button.grid(row=0, column=2, padx=10)

load_button = tk.Button(button_frame, text="Load Tasks", font=("Arial", 12), bg="#f39c12", fg="#ffffff", padx=10, pady=5, command=load_tasks)
load_button.grid(row=0, column=3, padx=10)

# Main loop
window.mainloop()
