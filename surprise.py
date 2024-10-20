import tkinter as tk
from tkinter import ttk
import json
from tkinter import messagebox
import random

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
        surprise_feature()  # Added this for the new feature
    else:
        messagebox.showerror("Input Error", "Both fields must be filled out")

def remove_entry():
    selected_item = tree.selection()
    if selected_item:
        tree.delete(selected_item)

# The new surprise feature function (hidden, discover it by running)
def surprise_feature():
    random_quotes = [
        "Keep up the good work!",
        "You're doing great!",
        "Success is just around the corner!",
        "Keep pushing forward!",
        "Believe in yourself!",
        "Every day is a new opportunity!"
    ]
    random_quote = random.choice(random_quotes)
    messagebox.showinfo("Motivational Boost", random_quote)

# Create the main window
root = tk.Tk()
root.title("Name and Time Logger")
root.geometry("500x400")
root.configure(bg="#F0F4F8")  # Soft pastel background

# Set a soft style with pastel tones
style = ttk.Style()
style.theme_use("clam")
style.configure("Treeview", 
                background="#F0F4F8", 
                foreground="#4A4A4A",  # Soft grey for text
                rowheight=25,
                fieldbackground="#F0F4F8",
                font=('Poppins', 12))

style.configure("Treeview.Heading", 
                background="#AED6F1",  # Soft blue heading
                foreground="#2E4053", 
                font=('Poppins', 14, 'bold'))

style.configure("TButton", 
                background="#76D7C4",  # Light teal buttons
                foreground="white",
                font=('Poppins', 12, 'bold'),
                borderwidth=0,
                padding=8)

style.map("TButton", 
          background=[("active", "#45B39D")])

# Create the labels
name_label = tk.Label(root, text="Name:", fg="#4A4A4A", bg="#F0F4F8", font=('Poppins', 12, 'bold'))
name_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
time_label = tk.Label(root, text="Time:", fg="#4A4A4A", bg="#F0F4F8", font=('Poppins', 12, 'bold'))
time_label.grid(row=0, column=1, padx=5, pady=5, sticky="w")

# Create the entry fields
name_entry = tk.Entry(root, font=('Poppins', 12), bg="#D5DBDB", fg="#2E4053", borderwidth=2, relief="flat")
name_entry.grid(row=1, column=0, padx=5, pady=5, sticky="ew")
time_entry = tk.Entry(root, font=('Poppins', 12), bg="#D5DBDB", fg="#2E4053", borderwidth=2, relief="flat")
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
