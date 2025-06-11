# ATM

 # Itachi ATM Simulation
 
 A simple Python script that simulates a basic ATM machine. Users can check their balance, deposit, and withdraw money after entering the correct PIN.

***Features*** <br>
  - PIN authentication for security
  - Check account balance
  - Deposit money
  - Withdraw money (with insufficient funds check)
  - Realistic transaction processing delays using ``` time.sleep() ```
  - Friendly prompts and messages

***How It Works*** <br>

  1. The script waits a few seconds to simulate an ATM booting up.
  2. The user is prompted to insert their card and enter their PIN.
  3. If the PIN is correct, the user can:
     - Check their balance
     - Deposit money
     - Withdraw money
  4. Each transaction simulates processing time for a more realistic experience.
  5. The script handles incorrect PINs and insufficient balance scenarios.

***Usage*** <br>
 1. Copy the following code into a Python file (e.g., atm.py):
  
    ```
    import time
    time.sleep(2)
    pin = 1234
    bal = 1000
    print("Welcome to Itachi Atm")
    time.sleep(3)
    print("Insert a your card")
    time.sleep(1)
    p = int(input("Enter a Pin:"))
    if pin == p:
        time.sleep(1)
        print("Transcation Processing.........")
        while True:
        time.sleep(4)
        print("1.Check Balance\n2.Desopit\n3.Withdrawal")
        opt = int(input("Enter a No:"))
        if opt == 1:
            time.sleep(1)
            print("Transcation Processing.........")
            time.sleep(3)
            print("Current balance $", bal)
            time.sleep(2)
            print("Remove your card\n Thanks for visiting a ATM")
            pass
        elif opt == 2:
            print("Transcation Processing.........")
            amt = int(input("Enter a amout to Deposit $ :"))
            bal += amt
            time.sleep(1)
            print("Your Desopit amount $", amt)
            time.sleep(1)
            print("Your current balance is $", bal)
            time.sleep(1)
            print("Deposit Successfully ")
            continue  
        elif opt == 3:
            print("Transcation Processing.........")
            amt = int(input("Enter a amout to Withdirwal $:"))
            if amt < bal:
                bal -= amt
                print("Trancsation procesing...")
                time.sleep(2)
                print("Collect you cash.....")
                time.sleep(2)
                print("Successfully Withdrwal cash\nPlease remove your atm card")
            elif amt > bal:
                print("Insufficient amount\nRemove your atm card\nThanks u for visiting atm")
            else:
                print("Trascation processing....")
                time.sleep(4)
                print("Invaild pin")
                break
    else:
        print("Trascation processing....")
        time.sleep(4)
        print("Invaild pin")

    ```
 3. Run the script:
     ```
     python atm.py
     ```
 4. Follow the on-screen instructions.

***Example Interaction*** <br>

 ```
  Welcome to Itachi Atm
  Insert a your card
  Enter a Pin: 1234
  Transcation Processing.........
  1.Check Balance
  2.Desopit
  3.Withdrawal
  Enter a No: 1
  Transcation Processing.........
  Current balance $ 1000
  Remove your card
  Thanks for visiting a ATM

 ```
***Notes*** <br>

  - The default PIN is 1234 and the initial balance is $1000.
  - Transactions are simulated with delays for realism.
  - The script does not persist data between runs.
  - There are some spelling mistakes in the prompts (e.g., "Desopit" instead of "Deposit", "Withdirwal" instead of "Withdrawal"). You can correct these for a more polished experience.



# 🏧 ATM Simulator (Python Tkinter)


A beginner-friendly ATM Machine simulation built with Python and Tkinter.
You can log in with a PIN, check your balance, deposit, withdraw, view transaction history, change your PIN, and even create a new account—all with a simple graphical interface!

---

## 🌟 Features

- **PIN-based Login:** Secure access for each user.
- **Multiple Users:** Start with 10 sample accounts.
- **Check Balance:** Instantly see your available funds.
- **Deposit & Withdraw:** Add or withdraw money, with clear feedback.
- **Transaction History:** View your last 10 transactions.
- **Change PIN:** Update your PIN securely.
- **Create Account:** Open a new account with a unique PIN.
- **Custom Icons:** Looks and feels like a real ATM!

---

## 🖼️ Screenshots

> **Tip:** Save your own screenshots as `login.png`, `menu.png`, and `balance.png` in a `screenshots` folder.
> Save your own screenshots as `login.png`, `menu.png`, and `history.png` in a `screenshots` folder.  
> Use `.ico` files for custom window icons (e.g., `Atm.ico`, `Balance.ico`, `Deposit.ico`).

| Login Screen | Main Menu | Transaction History |
|:------------:|:---------:|:------------------:|
| ![Login](screenshots/login.png) | ![Menu](screenshots/menu.png) | ![History](screenshots/history.png) |

**ATM Icon Example:**  
![ATM Icon](Image/Atm.ico)

### 1. Login Screen


### 2. Main Menu


### 3. Balance Display


---

## 🚀 How to Run

1. **Install Python** (if you don’t have it).
2. **Download the code** (`atm.py`) and (optionally) an icon file (`atm.ico`).
3. **Open a terminal** in the project folder.
4. **Run:**
    ```
    python ATM GUI.py
    ```

---

## 👤 User Accounts

Try logging in with these sample PINs:

| Name     | PIN   | Balance (₹) |
|----------|-------|-------------|
| Alice    | 1111  | 1200        |
| Bob      | 2222  | 1500        |
| Charlie  | 3333  | 900         |
| David    | 4444  | 2000        |
| Eva      | 5555  | 1100        |
| Frank    | 6666  | 800         |
| Grace    | 7777  | 1700        |
| Helen    | 8888  | 1300        |
| Ivan     | 9999  | 1400        |
| Jane     | 0000  | 1000        |

---

## 📝 How It Works

1. **Login:** Enter your 4-digit PIN to access your account.
2. **Main Menu:** Choose from Check Balance, Deposit, Withdraw, Transaction History, Change PIN, Create Account, Logout, or Exit.
3. **Transactions:** Follow prompts for deposits or withdrawals. All actions are confirmed with pop-up messages.
4. **History:** See your last 10 transactions, including deposits and withdrawals.
5. **Change PIN:** Enter and confirm a new 4-digit PIN.
6. **Create Account:** Enter a name, unique PIN, and initial deposit to open a new account.

---

## 🛠️ Code Overview

- **Tkinter GUI:** For all windows and dialogs.
- **User Data:** Stored as a list of dictionaries, each representing an account.
- **Icons:** Set with `root.iconbitmap("Image/Atm.ico")` and similar lines for each window (add your own `.ico` files).
- **Transaction History:** Each user has a `history` list updated after every deposit or withdrawal.

---
## 📂 File Structure


---

## 💡 Customization

- **Add/Remove Users:** Edit the `self.users` list in the code.
- **Change Icons:** Replace `.ico` files in the `Image/` folder and update icon paths in the code.
- **Improve UI:** Add more features, such as PIN reset by admin, or export transaction history.

---

## 📚 Learn More

- [ATM Simulation Project Example (PDF)](https://www.scribd.com/document/492185999/Atm-i-Python-Mini-Project)
- [Tkinter ATM Project on Kashipara](https://www.kashipara.com/project/idea/python/atm-project-gui-based-in-python-_3586.html)
- [Python GUI ATM Tutorial](https://pythongui.org/how-to-make-a-python-gui-for-an-atm-system/)
- [Tkinter Official Documentation](https://docs.python.org/3/library/tkinter.html)
- [Beginner Python Projects](https://www.kashipara.com/project/idea/python/atm-project-gui-based-in-python-_3586.html)
- [Python GUI ATM Tutorial](https://pythongui.org/how-to-make-a-python-gui-for-an-atm-system/)
- 
---

## 🏁 Start Coding and Have Fun!

---

> **Note:** This project is for educational purposes only. No real money is involved!

---
*Happy Coding!*


