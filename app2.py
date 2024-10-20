import tkinter as tk
from tkinter import ttk
import json

def save_data():
    """Save the Treeview data to a file."""
    items = []
    for child in tree.get_children():
        items.append(tree.item(child)["values"])
    with open('data.json', 'w') as f:
        json.dump(items, f)

def load_data():
    """Load data from the file into the Treeview."""
    try:
        with open('data.json', 'r') as f:
            items = json.load(f)
            for item in items:
                tree.insert("", "end", values=item)
    except FileNotFoundError:
        pass  # If the file doesn't exist, do nothing

def add_entry():
    name = name_entry.get()
    time = time_entry.get()
    if name and time:
        tree.insert("", "end", values=(name, time))
        name_entry.delete(0, tk.END)
        time_entry.delete(0, tk.END)

def remove_entry():
    selected_item = tree.selection()
    if selected_item:
        tree.delete(selected_item)

# Create the main window
root = tk.Tk()
root.title("Name and Time Logger")
root.geometry("500x400")
root.configure(bg="#1A1A1A")  # Dark background

# Set a modern style with bold, vibrant colors
style = ttk.Style()
style.theme_use("clam")
style.configure("Treeview", 
                background="#1A1A1A", 
                foreground="#F1C40F",  # Vibrant yellow for text
                rowheight=25,
                fieldbackground="#1A1A1A",
                font=('Segoe UI', 12))

style.configure("Treeview.Heading", 
                background="#E74C3C",  # Red heading background
                foreground="white", 
                font=('Segoe UI', 14, 'bold'))

style.configure("TButton", 
                background="#3498DB",  # Bright blue buttons
                foreground="white",
                font=('Segoe UI', 12, 'bold'),
                borderwidth=0,
                padding=8)

style.map("TButton", 
          background=[("active", "#2980B9")])

# Create the labels
name_label = tk.Label(root, text="Name:", fg="#F1C40F", bg="#1A1A1A", font=('Segoe UI', 12, 'bold'))
name_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
time_label = tk.Label(root, text="Time:", fg="#F1C40F", bg="#1A1A1A", font=('Segoe UI', 12, 'bold'))
time_label.grid(row=0, column=1, padx=5, pady=5, sticky="w")

# Create the entry fields
name_entry = tk.Entry(root, font=('Segoe UI', 12), bg="#333333", fg="white", borderwidth=2, relief="flat")
name_entry.grid(row=1, column=0, padx=5, pady=5, sticky="ew")
time_entry = tk.Entry(root, font=('Segoe UI', 12), bg="#333333", fg="white", borderwidth=2, relief="flat")
time_entry.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

# Create the add button
add_button = ttk.Button(root, text="Add Entry", command=add_entry)
add_button.grid(row=1, column=2, padx=5, pady=5, sticky="ew")

# Create the Treeview widget
tree = ttk.Treeview(root, columns=("Name", "Time"), show="headings")
tree.heading("Name", text="Name")
tree.heading("Time", text="Time")
tree.column("Name", anchor="center")
tree.column("Time", anchor="center")
tree.grid(row=2, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

# Create the remove button
remove_button = ttk.Button(root, text="Remove Entry", command=remove_entry)
remove_button.grid(row=3, column=0, columnspan=3, pady=10)

# Adjust grid layout for responsiveness
root.grid_rowconfigure(2, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)

# Load data when the app starts
load_data()

# Save data when the app closes
root.protocol("WM_DELETE_WINDOW", lambda: (save_data(), root.destroy()))

# Start the main event loop
root.mainloop()
