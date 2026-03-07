print('Simple IF \n')

password = input("enter Password : ")
entered_password = input("enter saved password : ")

if entered_password == password:
    print("Login successful \n")

    
print('if-else \n')
balance = int(input("Enter total Amount in the Account : "))
withdraw = int(input("Enter the Amount to Withdraw : "))

if withdraw <= balance:
    print("Transaction successful \n")
else:
    print("Insufficient balance \n")


print('elsif Ladder \n')

amount = int(input("Enter the Purchased Amount : "))

if amount >= 10000:
    print("20% discount \n")
elif amount >= 5000:
    print("10% discount \n")
elif amount >= 1000:
    print("5% discount \n")
else:
    print("No discount \n")

    
print("Nested - If")


age = int(input("enter Age : "))
degree = True

if age >= 21:
    if degree:
        print("Eligible for job interview \n")
    else:
        print("Degree required \n")
else:
    print("Age not eligible \n")
