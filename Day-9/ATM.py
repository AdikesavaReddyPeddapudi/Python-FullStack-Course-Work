data={
    '123456':{'pin':'1234','balance':4000,'history':[]},
    '234561':{'pin':'1234','balance':6000,'history':[]},
    '345612':{'pin':'1234','balance':8000,'history':[]},
    '456123':{'pin':'1234','balance':9000,'history':[]},
    }

def deposit(acc_num):
    print('--------------------------------------------')
    amount = int(input("Enter the amount: "))
    data[acc_num]['balance']+=amount
    print(f"{amount} is deposited successfully")
    check_balance(acc_num)
    data[acc_num]['history'].append(f"{amount} is deposited")
    print('--------------------------------------------')

    
def withdraw(acc_num):
    print('--------------------------------------------')
    amount = int(input("Enter the amount: "))
    if data[acc_num]['balance'] >= amount:
        data[acc_num]['balance']-=amount
        print(f"{amount} is withdraw successfully")
        check_balance(acc_num)
        data[acc_num]['history'].append(f"{amount} is withdraw")
        print('--------------------------------------------')
    else:
        print("Insuffient balance")

    
def change_pin():
    pass

def check_balance(acc_num):
    print('--------------------------------------------')
    print(f"Current Balance: {data[acc_num]['balance']}")
    print('--------------------------------------------')


def view_transactions(acc_num):
    if data[acc_num]['history']:
        print("-------Transaction History-----------")
        for i in data[acc_num]['history']:
            print(i)
        else:
            print("--------------End of the transactions---------")
    else:
        print("No Transactions")

def menu():
    print("[C]heck Balance")
    print("[D]eposit")
    print("[W]ithdraw")
    print("[V]iew Transactions")
    print("Change [P]in")
    print("[E]xit")




print("-----------Welcome to the ATM-----------")
acc_num = input("Enter the account number: ")
pin = input("Enter the pin: ")

if acc_num in data and data[acc_num]['pin']==pin:
    print("Login Successful")
    while True:
        menu()
        ch = input("Enter your choice: ").lower()
        if ch=='c':
            check_balance(acc_num)
        elif ch=='d':
            deposit(acc_num)
        elif ch=='w':
            withdraw(acc_num)
        elif ch=='v':
            view_transactions(acc_num)
        elif ch=='p':
            change_pin(acc_num)
        elif ch=='e':
            print("--------Thankyou----------")
            break
        else:
            print("Enter the valid choice")

else:
    print("Invalid Login")



    
