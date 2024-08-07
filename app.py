import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def add_item():
    name = name_entry.get()
    time = time_entry.get()
    if name and time:
        tree.insert("", tk.END, values=(name, time))
        name_entry.delete(0, tk.END)
        time_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter both name and time.")

def remove_item():
    selected_item = tree.selection()
    if selected_item:
        for item in selected_item:
            tree.delete(item)
    else:
        messagebox.showwarning("Selection Error", "Please select an item to remove.")

root = tk.Tk()
root.title("Reportschema")

# Configure root window
root.geometry("600x400")  # Set a default window size
root.resizable(True, True)  # Allow resizing

# Define styles
style = ttk.Style()
style.configure("TLabel",
                font=("Segoe UI", 12),
                background="#f4f4f4",
                foreground="#333")
style.configure("TEntry",
                padding=5,
                relief="flat",
                font=("Segoe UI", 12))
style.configure("TButton",
                padding=6,
                relief="flat",
                font=("Segoe UI", 12),
                background="#007bff",
                foreground="white")
style.map("TButton",
          background=[("active", "#0056b3")])

# Treeview styles
style.configure("Treeview",
                font=("Segoe UI", 12),  # Font size for treeview items
                background="#ffffff",
                foreground="#000000",
                rowheight=30)  # Increase row height for better readability

style.configure("Treeview.Heading",
                font=("Segoe UI", 14))  # Font size for column headings

# Entry Widgets
name_label = ttk.Label(root, text="Name")
name_label.grid(row=0, column=0, sticky=tk.W, padx=10, pady=10)
name_entry = ttk.Entry(root)
name_entry.grid(row=1, column=0, sticky=tk.EW, padx=10, pady=5)

time_label = ttk.Label(root, text="Time")
time_label.grid(row=0, column=1, sticky=tk.W, padx=10, pady=10)
time_entry = ttk.Entry(root)
time_entry.grid(row=1, column=1, sticky=tk.EW, padx=10, pady=5)

# Buttons
add_button = ttk.Button(root, text="Add client", command=add_item)
add_button.grid(row=2, column=0, columnspan=2, sticky=tk.EW, padx=10, pady=10)

remove_button = ttk.Button(root, text="Remove client", command=remove_item)
remove_button.grid(row=3, column=0, columnspan=2, sticky=tk.EW, padx=10, pady=10)

# Treeview
columns = ("Name", "Time")
tree = ttk.Treeview(root, columns=columns, show="headings")

# Set column headings
tree.heading("Name", text="Name")
tree.heading("Time", text="Time")

# Configure column widths and alignment
tree.column("Name", width=250, anchor=tk.CENTER)
tree.column("Time", width=150, anchor=tk.CENTER)

# Grid configuration for resizing
tree.grid(row=4, column=0, columnspan=2, sticky=tk.NSEW, padx=10, pady=10)

# Configure row and column weights to make the Treeview expand
root.grid_rowconfigure(4, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

# Set a modern color for the root window
root.configure(bg="#f4f4f4")

root.mainloop()
