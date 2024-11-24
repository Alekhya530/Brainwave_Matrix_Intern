import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# Sample user credentials for authentication
USER_CREDENTIALS = {"admin": "brainwave"}

# Inventory data structure
inventory = {}

# Function to authenticate user
def authenticate(username, password):
    return USER_CREDENTIALS.get(username) == password

# Function to add a product to the inventory
def add_product():
    product_id = product_id_entry.get().strip()
    product_name = product_name_entry.get().strip()
    quantity = quantity_entry.get().strip()
    
    if not product_id or not product_name or not quantity.isdigit():
        messagebox.showerror("Error", "Invalid input. Ensure all fields are filled correctly.")
        return
    
    quantity = int(quantity)
    if product_id in inventory:
        messagebox.showwarning("Warning", "Product ID already exists. Use Edit to update.")
    else:
        inventory[product_id] = {"name": product_name, "quantity": quantity}
        messagebox.showinfo("Success", "Product added successfully.")
        refresh_inventory()

# Function to edit a product
def edit_product():
    product_id = product_id_entry.get().strip()
    product_name = product_name_entry.get().strip()
    quantity = quantity_entry.get().strip()
    
    if product_id not in inventory:
        messagebox.showerror("Error", "Product ID not found.")
        return
    
    if not product_name or not quantity.isdigit():
        messagebox.showerror("Error", "Invalid input. Ensure all fields are filled correctly.")
        return
    
    inventory[product_id]["name"] = product_name
    inventory[product_id]["quantity"] = int(quantity)
    messagebox.showinfo("Success", "Product updated successfully.")
    refresh_inventory()

# Function to delete a product
def delete_product():
    product_id = product_id_entry.get().strip()
    
    if product_id in inventory:
        del inventory[product_id]
        messagebox.showinfo("Success", "Product deleted successfully.")
        refresh_inventory()
    else:
        messagebox.showerror("Error", "Product ID not found.")

# Function to refresh inventory display
def refresh_inventory():
    for row in inventory_table.get_children():
        inventory_table.delete(row)
    
    for product_id, details in inventory.items():
        inventory_table.insert("", "end", values=(product_id, details["name"], details["quantity"]))

# Function to show low-stock products
def show_low_stock():
    low_stock_items = [f"{pid}: {details['name']} (Qty: {details['quantity']})" 
                       for pid, details in inventory.items() if details["quantity"] < 5]
    
    if low_stock_items:
        messagebox.showinfo("Low Stock Alert", "\n".join(low_stock_items))
    else:
        messagebox.showinfo("Low Stock Alert", "All products have sufficient stock.")

# Authentication screen
def show_main_window():
    auth_window.destroy()
    
    global main_window, product_id_entry, product_name_entry, quantity_entry, inventory_table
    main_window = tk.Tk()
    main_window.title("Inventory Management System")
    
    # Input fields
    tk.Label(main_window, text="Product ID").grid(row=0, column=0, padx=10, pady=5)
    product_id_entry = tk.Entry(main_window)
    product_id_entry.grid(row=0, column=1, padx=10, pady=5)
    
    tk.Label(main_window, text="Product Name").grid(row=1, column=0, padx=10, pady=5)
    product_name_entry = tk.Entry(main_window)
    product_name_entry.grid(row=1, column=1, padx=10, pady=5)
    
    tk.Label(main_window, text="Quantity").grid(row=2, column=0, padx=10, pady=5)
    quantity_entry = tk.Entry(main_window)
    quantity_entry.grid(row=2, column=1, padx=10, pady=5)
    
    # Buttons
    tk.Button(main_window, text="Add Product", command=add_product).grid(row=3, column=0, padx=10, pady=5)
    tk.Button(main_window, text="Edit Product", command=edit_product).grid(row=3, column=1, padx=10, pady=5)
    tk.Button(main_window, text="Delete Product", command=delete_product).grid(row=3, column=2, padx=10, pady=5)
    tk.Button(main_window, text="Show Low Stock", command=show_low_stock).grid(row=4, column=0, columnspan=3, pady=5)
    
    # Inventory table
    inventory_table = ttk.Treeview(main_window, columns=("ID", "Name", "Quantity"), show="headings")
    inventory_table.heading("ID", text="Product ID")
    inventory_table.heading("Name", text="Product Name")
    inventory_table.heading("Quantity", text="Quantity")
    inventory_table.grid(row=5, column=0, columnspan=3, padx=10, pady=10)
    
    main_window.mainloop()

# Authentication window
auth_window = tk.Tk()
auth_window.title("Login")

tk.Label(auth_window, text="Username").grid(row=0, column=0, padx=10, pady=5)
username_entry = tk.Entry(auth_window)
username_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(auth_window, text="Password").grid(row=1, column=0, padx=10, pady=5)
password_entry = tk.Entry(auth_window, show="*")
password_entry.grid(row=1, column=1, padx=10, pady=5)

def login():
    username = username_entry.get().strip()
    password = password_entry.get().strip()
    if authenticate(username, password):
        show_main_window()
    else:
        messagebox.showerror("Error", "Invalid credentials!")

tk.Button(auth_window, text="Login", command=login).grid(row=2, column=0, columnspan=2, pady=10)

auth_window.mainloop()
