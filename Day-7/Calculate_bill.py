products={1:("Rice",60),
           2:("Wheat Flour",45),
           3:("Sugar",40),
           4:("Milk",25),
           5:("Eggs(12 pcs)",70),
           6:("Cooking Oil",190),
           7:("Tea Powder",90),
           8:("salt",20),
           9:("Bread",30),
           10:("soap",30)
           }

def display_product():
    print(" \n Available Products : ")
    print("Index   product   Price")

    for i in products:
        name,price=products[i]
    print(i,"  ",name,"   ",price)

def get_user_input():
    indexes = input("\n Enter product indexes : ")
    selected = list(map(int,indexes.split()))
    return selected

def cal_bill(selected):
    total=0
    print("\n selected items : ")

    for i in selected:
        if i in products:
            name,price=products[i]
            print(name," - ",price)
            total += price

    print(" \n total bill =",total)

print("----------Welcome to Grocery Store ----------")
display_product()
selected_items=get_user_input()
cal_bill(selected_items)