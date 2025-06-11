import tkinter as tk
from tkinter import messagebox

class ATM:
    def __init__(self,root):
        self.root=root
        self.root.title("ATM Machine")
        self.users = [
            {"name": "Alice", "pin": "1111", "balance":1200},
            {"name": "Bob", "pin": "2222", "balance":1500},
            {"name": "Charlie", "pin": "3333", "balance":900},
            {"name": "David", "pin": "4444", "balance":2000},
            {"name": "Eva", "pin": "5555", "balance":1100},
            {"name": "Frank", "pin": "6666", "balance":800},
            {"name": "Grace", "pin": "7777", "balance":1700},
            {"name": "Helen", "pin": "8888", "balance":1300},
            {"name": "Ivan", "pin": "9999", "balance":1400},
            {"name": "Jane", "pin": "0000", "balance":1000}
        ]
        self.show_login()
        
    def process_transaction(self, next_action):
        self.clear_window()
        tk.Label(self.root,text="Transaction is processing...",fg="blue",font=("Arial", 12)).pack(pady=30)
        self.root.after(2000,next_action)  # Wait 2 seconds, then call the action

    def show_login(self):
        self.clear_window()
        tk.Label(self.root,text="Enter PIN:",font=("Arial", 12)).pack(pady=10)
        self.pin_entry=tk.Entry(self.root,show="*",width=15,font=("Arial",12))
        self.pin_entry.pack(pady=5)
        tk.Button(self.root,text="Login",activebackground="green",activeforeground='white',command=self.check_pin).pack(pady=5)
        tk.Button(self.root,text="Clear",activebackground="yellow",activeforeground='white',command=lambda:self.pin_entry.delete(0,tk.END)).pack(pady=5)
        tk.Button(self.root,text="Cancel",activebackground="red",activeforeground='white',command=self.root.destroy).pack(padx=2,pady=5)

    def check_pin(self):
        pin=self.pin_entry.get()
        for user in self.users:
            if user["pin"]==pin:
                self.current_user=user
                self.show_menu()
                return
        messagebox.showerror("Login Failed","Invalid PIN.")

    def show_menu(self):
        self.clear_window()
        self.root.iconbitmap("D:/Img/atm_22180 (1).ico")  
        tk.Label(self.root,text="Welcome to ATM", font=("Arial", 14)).pack(pady=10)
        tk.Label(self.root,text=f"User name:{self.current_user['name']}",font=("Arial", 14)).pack(pady=10)
        tk.Button(self.root,text="Check Balance",width=20,command=lambda:self.process_transaction(self.display_balance)).pack(pady=5)
        tk.Button(self.root,text="Deposit",width=20,command=self.deposit_window).pack(pady=5)
        tk.Button(self.root,text="Withdraw",width=20,command=self.withdraw_window).pack(pady=5)
        tk.Button(self.root,text="Logout",width=20,command=self.show_login).pack(pady=5)
        tk.Button(self.root,text="Exit",width=20,command=self.root.destroy).pack(pady=5)

    def display_balance(self):
        self.clear_window()
        tk.Label(self.root,text=f"Your balance is: ₹{self.current_user['balance']}",font=("Arial",14)).pack(pady=15)
        tk.Button(self.root,text="Back",command=self.show_menu).pack(pady=10)

    def deposit_window(self):
        self.clear_window()
        self.root.iconbitmap("D:/Img/deposit_money_cash_banking_bank_icon_262091.ico") 
        tk.Label(self.root,text="Enter amount to deposit:",font=("Arial",12)).pack(pady=10)
        self.deposit_entry=tk.Entry(self.root,width=15,font=("Arial",12))
        self.deposit_entry.pack(pady=5)
        tk.Button(self.root,text="Deposit",command=self.deposit_amount).pack(pady=10)
        tk.Button(self.root,text="Cancel",command=lambda: self.deposit_entry.delete(0,tk.END)).pack(pady=5)
        tk.Button(self.root,text="Back",command=self.show_menu).pack(pady=5)
     
    def deposit_amount(self):
        try:
            amount=int(self.deposit_entry.get())
            if amount>0:
                self.process_transaction(lambda:self.finish_deposit(amount))
            else:
                messagebox.showerror("Error","Enter a positive amount.")
                self.deposit_window()
        except ValueError:
            messagebox.showerror("Error","Invalid input.")
            self.deposit_window()

    def finish_deposit(self, amount):
        self.current_user["balance"]+= amount
        messagebox.showinfo("Success",f"Deposited ₹{amount}")
        self.show_menu()

    def withdraw_window(self):
        self.clear_window()
        self.root.iconbitmap("D:/Img/banking_business_payment_cash_finance_money_coin_icon_254032.ico")
        tk.Label(self.root,text="Enter amount to withdraw:",font=("Arial", 12)).pack(pady=10)
        self.withdraw_entry=tk.Entry(self.root,width=15,font=("Arial", 12))
        self.withdraw_entry.pack(pady=5)
        tk.Button(self.root,text="Withdraw",command=self.withdraw_amount).pack(pady=10)
        tk.Button(self.root,text="Cancel",command=lambda: self.withdraw_entry.delete(0, tk.END)).pack(pady=5)
        tk.Button(self.root,text="Back",command=self.show_menu).pack(pady=5)

    def withdraw_amount(self):
        try:
            amount=int(self.withdraw_entry.get())
            if 0<amount<=self.current_user['balance']:
                self.process_transaction(lambda:self.finish_withdraw(amount))
            else:
                messagebox.showerror("Error","Invalid amount or insufficient balance.")
                self.withdraw_window()
        except ValueError:
            messagebox.showerror("Error","Invalid input.")
            self.withdraw_window()

    def finish_withdraw(self, amount):
        self.current_user['balance']-=amount
        messagebox.showinfo("Success",f"Withdrawal ₹{amount}")
        self.show_menu()
    
    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("350x350")
    root.iconbitmap("/ATMImage/atm_22180.ico")  # Uncomment and set your icon path if needed
    root.resizable(False, False)
    app = ATM(root)
    root.mainloop()
