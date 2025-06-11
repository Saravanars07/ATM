import tkinter as tk
from tkinter import messagebox
import datetime

class ATM:
    def __init__(self,root):
        self.root=root
        self.root.title("ATM Machine")
        self.users=[
            {"name": "Alice","pin": "1111","balance":1200},
            {"name": "Bob","pin":"2222","balance":1500},
            {"name": "Charlie","pin":"3333","balance":900},
            {"name": "David","pin":"4444","balance":2000},
            {"name": "Eva","pin":"5555","balance":1100},
            {"name": "Frank","pin":"6666","balance":800},
            {"name": "Grace","pin":"7777","balance":1700},
            {"name": "Helen","pin":"8888","balance":1300},
            {"name": "Ivan","pin":"9999","balance":1400},
            {"name": "Jane","pin":"0000","balance":1000}
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
                self.current_user=user  # This must be the actual dict from self.users
                self.show_menu()
                return
        messagebox.showerror("Login Failed","Invalid PIN.")
        
    def show_menu(self):
        self.clear_window()
        #self.root.title("ATM Machine")
        #self.root.iconbitmap("Image/Atm.ico")
        tk.Label(self.root,text="Welcome to ATM", font=("Arial", 14)).pack(pady=10)
        tk.Label(self.root,text=f"User name:{self.current_user['name']}",font=("Arial", 14)).pack(pady=10)
        tk.Button(self.root,text="Check Balance",width=20,command=lambda:self.process_transaction(self.display_balance)).pack(pady=5)
        tk.Button(self.root,text="Deposit",width=20,command=self.deposit_window).pack(pady=5)
        tk.Button(self.root,text="Withdraw",width=20,command=self.withdraw_window).pack(pady=5)
        tk.Button(self.root, text="Transaction History",width=20,command=lambda:self.process_transaction(self.show_history)).pack(pady=5)
        tk.Button(self.root,text="Change PIN",width=20,command=lambda:self.process_transaction(self.change_pin_window)).pack(pady=5)
        tk.Button(self.root, text="Create Account",width=20,command=lambda:self.process_transaction(self.create_account_window)).pack(pady=5)
        tk.Button(self.root,text="Logout",width=20,command=self.show_login).pack(pady=5)
        tk.Button(self.root,text="Exit",width=20,command=self.root.destroy).pack(pady=5)

    def display_balance(self):
        self.clear_window()
        #self.root.title("Check Balance")
        #self.root.iconbitmap("Image/Balance.ico") 
        tk.Label(self.root,text=f"Your balance is: ₹{self.current_user['balance']}",font=("Arial",14)).pack(pady=15)
        tk.Button(self.root,text="Back",command=lambda:self.process_transaction(self.show_menu)).pack(pady=10)

    def deposit_window(self):
        self.clear_window()
        #self.root.title("Deposit")
        #self.root.iconbitmap("Image/Deposit.ico") 
        tk.Label(self.root,text="Enter amount to deposit:",font=("Arial",12)).pack(pady=10)
        self.deposit_entry=tk.Entry(self.root,width=15,font=("Arial",12))
        self.deposit_entry.pack(pady=5)
        tk.Button(self.root,text="Deposit",command=self.deposit_amount).pack(pady=10)
        tk.Button(self.root,text="Cancel",command=lambda: self.deposit_entry.delete(0,tk.END)).pack(pady=5)
        tk.Button(self.root,text="Back",command=lambda:self.process_transaction(self.show_menu)).pack(pady=5)
     
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
        #self.root.title("Withdrawal")
        #self.root.iconbitmap("Image/Withdrawal.ico")
        tk.Label(self.root,text="Enter amount to withdraw:",font=("Arial", 12)).pack(pady=10)
        self.withdraw_entry=tk.Entry(self.root,width=15,font=("Arial", 12))
        self.withdraw_entry.pack(pady=5)
        tk.Button(self.root,text="Withdraw",command=self.withdraw_amount).pack(pady=10)
        tk.Button(self.root,text="Cancel",command=lambda: self.withdraw_entry.delete(0, tk.END)).pack(pady=5)
        tk.Button(self.root,text="Back",command=lambda:self.process_transaction(self.show_menu)).pack(pady=5)

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

    def change_pin_window(self):
        self.clear_window()
        #self.root.title("Change pin")
        #self.root.iconbitmap("Image/Pin.ico")
        tk.Label(self.root,text=f"User name:{self.current_user['name']}",font=("Arial",14)).pack(pady=10)
        tk.Label(self.root,text="Enter new PIN:",font=("Arial", 12)).pack(pady=10)
        self.new_pin_entry=tk.Entry(self.root,show="*",width=15,font=("Arial",12))
        self.new_pin_entry.pack(pady=5)
        tk.Label(self.root,text="Confirm new PIN:",font=("Arial",12)).pack(pady=10)
        self.confirm_pin_entry=tk.Entry(self.root,show="*",width=15,font=("Arial",12))
        self.confirm_pin_entry.pack(pady=5)
        tk.Button(self.root,text="Submit",command=self.change_pin).pack(pady=10)
        tk.Button(self.root,text="Cancel",command=self.pin_cancel).pack(pady=5)
        tk.Button(self.root,text="Back",command=lambda:self.process_transaction(self.show_menu)).pack(pady=5)

    def change_pin(self):
        new_pin=self.new_pin_entry.get()
        confirm_pin=self.confirm_pin_entry.get()
        if new_pin==confirm_pin and len(new_pin) == 4 and new_pin.isdigit():
            self.current_user["pin"]=new_pin
            print("PIN changed to:",self.current_user["pin"])  # Debugging line
            messagebox.showinfo("Success", "PIN changed successfully!")
            self.show_menu()
        else:
            messagebox.showerror("Error", "PINs do not match or are invalid.")
            self.change_pin_window()

    def pin_cancel(self):
        self.new_pin_entry.delete(0,tk.END)
        self.confirm_pin_entry.delete(0,tk.END)

    # When initializing users, add an empty history list:
    # {"name": ..., "pin": ..., "balance": ..., "history": []}

    def finish_deposit(self,amount):
        self.current_user["balance"]+=amount
        # Add to history
        self.current_user.setdefault("history",[]).append(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}-Deposited ₹{amount}||Avaliable Balance ₹ {self.current_user["balance"]}")
        messagebox.showinfo("Success", f"Deposited ₹{amount}")
        self.show_menu()

    def finish_withdraw(self,amount):
        self.current_user['balance']-=amount
        self.current_user.setdefault("history", []).append(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}-Withdrewal ₹{amount}||Avaliable Balance ₹{self.current_user["balance"]}")
        messagebox.showinfo("Success", f"Withdrawal ₹{amount}")
        self.show_menu()

    def show_history(self):
        self.clear_window()
        #self.root.title("Transaction History")
        #self.root.iconbitmap("Image/History.ico")
        tk.Label(self.root,text="Transaction History",font=("Arial",14)).pack(pady=10)
        history = self.current_user.get("history",[])
        if not history:
            tk.Label(self.root,text="No transactions yet.",font=("Arial",12)).pack(pady=5)
        else:
            for entry in history[-10:]:  # Show last 10 transactions
                tk.Label(self.root,text=entry,font=("Arial", 10),anchor="w",justify="left").pack(fill="x")
        tk.Button(self.root,text="Back",command=lambda:self.process_transaction(self.show_menu)).pack(pady=10)

    def create_account_window(self):
        self.clear_window()
        #self.root.title("Create Account")
        #self.root.iconbitmap("Image/Account.ico")
        tk.Label(self.root,text="Create New Account",font=("Arial",14)).pack(pady=10)
        tk.Label(self.root,text="Name:",font=("Arial",12)).pack()
        self.new_name_entry=tk.Entry(self.root,width=20,font=("Arial",12))
        self.new_name_entry.pack(pady=2)
        tk.Label(self.root,text="PIN (4 digits):",font=("Arial",12)).pack()
        self.new_pin_entry=tk.Entry(self.root,show="*",width=20,font=("Arial",12))
        self.new_pin_entry.pack(pady=2)
        tk.Label(self.root,text="Initial Deposit:",font=("Arial",12)).pack()
        self.new_balance_entry=tk.Entry(self.root,width=20,font=("Arial",12))
        self.new_balance_entry.pack(pady=2)
        tk.Button(self.root,text="Create",command=self.create_account).pack(pady=10)
        tk.Button(self.root,text="Cancel",command=self.create_cancel).pack(pady=5)
        tk.Button(self.root,text="Back",command=lambda:self.process_transaction(self.show_menu)).pack(pady=5)
        tk.Button(self.root,text="Exit",command=self.show_login).pack(pady=5)

    def create_cancel(self):
        self.new_name_entry.delete(0,tk.END)
        self.new_pin_entry.delete(0,tk.END)
        self.new_balance_entry.delete(0,tk.END)
        
    def create_account(self):
        name=self.new_name_entry.get()
        pin=self.new_pin_entry.get()
        try:
            balance=int(self.new_balance_entry.get())
        except ValueError:
            messagebox.showerror("Error","Invalid deposit amount.")
            self.create_account_window()
            return
        if len(pin)==4 and pin.isdigit() and balance>=0 and name:
            if any(user["pin"]==pin for user in self.users):
                messagebox.showerror("Error","PIN already exists.")
                self.create_account_window()
            else:
                self.users.append({"name":name,"pin":pin,"balance":balance,"history":[]})
                messagebox.showinfo("Success","Account created successfully!")
                self.show_login()
        else:
            messagebox.showerror("Error", "Invalid input.")
            self.create_account_window()

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("400x400")
    root.iconbitmap("Image/Atm.ico")  # Uncomment and set your icon path if needed
    root.resizable(False, False)
    app = ATM(root)
    root.mainloop()
    
