import tkinter as tk
from tkinter import messagebox

# ATM Class with simple GUI using Tkinter
class ATM:
    def __init__(self, master):
        self.master = master
        self.master.title("ATM Machine")
        self.master.geometry("300x400")
        
        # Predefined users and balances
        self.users = {'user1': {'pin': 1234, 'balance': 1000},
                      'user2': {'pin': 5678, 'balance': 1500}}
        self.logged_in_user = None
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.master, text="Enter Username:")
        self.label.pack(pady=10)

        self.username_entry = tk.Entry(self.master)
        self.username_entry.pack(pady=5)

        self.label_pin = tk.Label(self.master, text="Enter PIN:")
        self.label_pin.pack(pady=10)

        self.pin_entry = tk.Entry(self.master, show="*")
        self.pin_entry.pack(pady=5)

        self.login_button = tk.Button(self.master, text="Login", command=self.authenticate_user)
        self.login_button.pack(pady=20)

    def authenticate_user(self):
        user = self.username_entry.get()
        pin = self.pin_entry.get()

        # Authenticate
        if user in self.users and self.users[user]['pin'] == int(pin):
            self.logged_in_user = user
            messagebox.showinfo("Success", "Login successful!")
            self.show_menu()
        else:
            messagebox.showerror("Error", "Incorrect username or PIN")

    def show_menu(self):
        # Clear login fields
        for widget in self.master.winfo_children():
            widget.destroy()

        self.label = tk.Label(self.master, text="Welcome to the ATM!")
        self.label.pack(pady=20)

        self.balance_button = tk.Button(self.master, text="Check Balance", command=self.check_balance)
        self.balance_button.pack(pady=10)

        self.deposit_button = tk.Button(self.master, text="Deposit", command=self.deposit)
        self.deposit_button.pack(pady=10)

        self.withdraw_button = tk.Button(self.master, text="Withdraw", command=self.withdraw)
        self.withdraw_button.pack(pady=10)

        self.exit_button = tk.Button(self.master, text="Exit", command=self.master.quit)
        self.exit_button.pack(pady=20)

    def check_balance(self):
        balance = self.users[self.logged_in_user]['balance']
        messagebox.showinfo("Balance", f"Your current balance is: {balance}")

    def deposit(self):
        amount = self.prompt_amount("Deposit")
        if amount > 0:
            self.users[self.logged_in_user]['balance'] += amount
            messagebox.showinfo("Deposit", f"Successfully deposited {amount}.")
        else:
            messagebox.showerror("Error", "Enter a valid amount!")

    def withdraw(self):
        amount = self.prompt_amount("Withdraw")
        if amount > 0:
            if amount <= self.users[self.logged_in_user]['balance']:
                self.users[self.logged_in_user]['balance'] -= amount
                messagebox.showinfo("Withdraw", f"Successfully withdrew {amount}.")
            else:
                messagebox.showerror("Error", "Insufficient balance!")
        else:
            messagebox.showerror("Error", "Enter a valid amount!")

    def prompt_amount(self, transaction_type):
        # Popup to get amount from user
        amount = tk.simpledialog.askfloat(transaction_type, f"Enter amount to {transaction_type.lower()}:")
        return amount if amount is not None else 0


# Main function to run the GUI ATM
if __name__ == "__main__":
    root = tk.Tk()
    atm = ATM(root)
    root.mainloop()
