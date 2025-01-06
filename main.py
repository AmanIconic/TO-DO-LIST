import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task != "":
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task!")

def delete_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete!")

def clear_all_tasks():
    task_listbox.delete(0, tk.END)

root = tk.Tk()
root.title("To-Do List App")

task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task", command=add_task, width=15, bg="lightblue")
add_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Task", command=delete_task, width=15, bg="lightcoral")
delete_button.pack(pady=5)

clear_button = tk.Button(root, text="Clear All Tasks", command=clear_all_tasks, width=15, bg="lightgreen")
clear_button.pack(pady=5)

task_listbox = tk.Listbox(root, width=40, height=10)
task_listbox.pack(pady=10)

root.mainloop()
