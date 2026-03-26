print("----- Welcome to Grocery Store -----")

products = ["Rice", "Wheat Flour", "Sugar", "Milk", "Eggs (12 pcs)",
            "Cooking Oil", "Tea Powder", "Salt", "Bread", "Soap"]

prices = [60, 45, 40, 25, 70, 130, 90, 20, 30, 25]

print("----------\nAvailable Products------------")
print("Index".ljust(6," "),"Product".ljust(6," "),"Price".ljust(6," "))

for i in range(len(products)):
    print(str(i+1).ljust(6," "), products[i].ljust(15," "),str(prices[i]).ljust(6," "))
3
indexes = input("\nEnter product indexes separated by space: ")

selected = list(map(int, indexes.split()))

total = 0

print("\nSelected Items:")

for i in selected:
    product = products[i-1]
    price = prices[i-1]
    
    print(product.ljust(15," "), "-", price)
    
    total = total + price

print("\nTotal Bill =", total)