import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# Sample product list (product_name: [quantity, price])
products = {}

# Login credentials
USERNAME = "saniya"
PASSWORD = "161224"

# Function to validate login
def validate_login():
    username = entry_username.get()
    password = entry_password.get()
    
    if username == USERNAME and password == PASSWORD:
        login_window.destroy()
        main_app()
    else:
        messagebox.showerror("Error", "Invalid username or password!")

# Function to add a product
def add_product():
    product_name = entry_product_name.get()
    quantity = int(entry_quantity.get())
    price = float(entry_price.get())

    if product_name in products:
        messagebox.showinfo("Error", "Product already exists!")
    else:
        products[product_name] = [quantity, price]
        messagebox.showinfo("Success", f"Product '{product_name}' added!")
        clear_entries()

# Function to edit a product
def edit_product():
    product_name = entry_product_name.get()
    quantity = int(entry_quantity.get())
    price = float(entry_price.get())

    if product_name in products:
        products[product_name] = [quantity, price]
        messagebox.showinfo("Success", f"Product '{product_name}' updated!")
        clear_entries()
    else:
        messagebox.showinfo("Error", "Product not found!")

# Function to delete a product
def delete_product():
    product_name = entry_product_name.get()

    if product_name in products:
        del products[product_name]
        messagebox.showinfo("Success", f"Product '{product_name}' deleted!")
        clear_entries()
    else:
        messagebox.showinfo("Error", "Product not found!")

# Function to generate reports
def generate_report():
    report = ""
    for product_name, (quantity, price) in products.items():
        if quantity < 10:
            report += f"Low stock alert for {product_name} (Quantity: {quantity})\n"
    if not report:
        report = "No low stock alerts!"
    
    messagebox.showinfo("Inventory Report", report)

# Function to clear input fields
def clear_entries():
    entry_product_name.delete(0, tk.END)
    entry_quantity.delete(0, tk.END)
    entry_price.delete(0, tk.END)

# Main application
def main_app():
    global entry_product_name, entry_quantity, entry_price

    window = tk.Tk()
    window.title("Inventory Management System")

    # Labels and Entries
    tk.Label(window, text="Product Name").grid(row=0, column=0)
    entry_product_name = tk.Entry(window)
    entry_product_name.grid(row=0, column=1)

    tk.Label(window, text="Quantity").grid(row=1, column=0)
    entry_quantity = tk.Entry(window)
    entry_quantity.grid(row=1, column=1)

    tk.Label(window, text="Price").grid(row=2, column=0)
    entry_price = tk.Entry(window)
    entry_price.grid(row=2, column=1)

    # Buttons
    btn_add = tk.Button(window, text="Add Product", command=add_product)
    btn_add.grid(row=3, column=0)

    btn_edit = tk.Button(window, text="Edit Product", command=edit_product)
    btn_edit.grid(row=3, column=1)

    btn_delete = tk.Button(window, text="Delete Product", command=delete_product)
    btn_delete.grid(row=4, column=0)

    btn_report = tk.Button(window, text="Generate Report", command=generate_report)
    btn_report.grid(row=4, column=1)

    window.mainloop()

# Login window
login_window = tk.Tk()
login_window.title("Login")

# Labels
tk.Label(login_window, text="Username").grid(row=0, column=0)
tk.Label(login_window, text="Password").grid(row=1, column=0)

# Entry fields for username and password
entry_username = tk.Entry(login_window)
entry_password = tk.Entry(login_window, show="*")
entry_username.grid(row=0, column=1)
entry_password.grid(row=1, column=1)

# Login button
btn_login = tk.Button(login_window, text="Login", command=validate_login)
btn_login.grid(row=2, column=1)

login_window.mainloop()
