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

A simple, interactive ATM machine simulation using Python and Tkinter!  
You can check your balance, deposit, withdraw, and log out—all with a friendly graphical interface.

---

## 🌟 Features

- **PIN-based Login:** Secure access using a 4-digit PIN.
- **Multiple Users:** 10 sample accounts to try.
- **Check Balance:** See how much money you have.
- **Deposit & Withdraw:** Add or take out money, with instant feedback.
- **Easy Navigation:** Clear buttons and prompts.
- **Custom Icon:** Looks more like a real ATM!

---

## 🖼️ Screenshots

> **Tip:** Save your own screenshots as `login.png`, `menu.png`, and `balance.png` in a `screenshots` folder.

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

## 📝 How it Works

1. **Enter your PIN** on the login screen.
2. **Main menu** appears with options:  
   - Check Balance  
   - Deposit  
   - Withdraw  
   - Logout/Exit
3. **Choose an action** and follow the prompts.
4. **Logout** to return to the login screen.

---

## 🛠️ Code Highlights

- **Tkinter** for the GUI
- **List of dictionaries** for user data
- **Error handling** for invalid PINs and amounts
- **Custom icon** (optional, set your `.ico` file path in the code)

---

## 📂 File Structure


---

## 💡 Customization

- **Change users:** Edit the `self.users` list in the code.
- **Change icon:** Replace the path in `root.iconbitmap("path/to/atm.ico")`.
- **Add features:** Try adding PIN change, transaction history, or account creation!

---

## 📚 Learn More

- [ATM Simulation Project Example (PDF)](https://www.scribd.com/document/492185999/Atm-i-Python-Mini-Project)[1]
- [Tkinter ATM Project on Kashipara](https://www.kashipara.com/project/idea/python/atm-project-gui-based-in-python-_3586.html)[2]
- [Python GUI ATM Tutorial](https://pythongui.org/how-to-make-a-python-gui-for-an-atm-system/)[7]

---

## 🏁 Start Coding and Have Fun!

---

> **Note:** This is a learning project. No real money is involved!


