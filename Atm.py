import time
time.sleep(2)
pin=1234
bal=1000
print("Welcome to Itachi Atm")
time.sleep(3)
print("Insert a  your card")
time.sleep(1)
p=int(input("Enter a Pin:"))
if pin==p:
    time.sleep(1)
    print("Transcation Processing.........")
    while True:
        time.sleep(4)
        print("1.Check Balance\n2.Desopit\n3.Withdrawal")
        opt=int(input("Enter a No:"))
        if opt==1:
            time.sleep(1)
            print("Transcation Processing.........")
            time.sleep(3)
            print("Current balance $",bal)
            time.sleep(2)
            print("Remove your card\n Thanks for visiting a ATM")
            pass
        elif opt==2:
            print("Transcation Processing.........")
            amt=int(input("Enter a amout to Deposit $ :"))
            bal +=amt
            print("Transcation Processing.........")
            time.sleep(3)
            print("Your Desopit amount $",amt)
            time.sleep(1)
            print("Your current balance is $",bal)
            time.sleep(1)
            print("Deposit Successfully ")
            continue  
        elif opt==3:
            print("Transcation Processing.........")
            amt=int(input("Enter a amout to Withdirwal $:"))
            if amt<bal:
                bal -=amt
                print("Trancsation procesing...")
                time.sleep(2)
                print("Collect you cash.....")
                time.sleep(2)
                print("Successfully Withdrwal cash\nPlease remove your atm card")
            elif amt>bal:
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