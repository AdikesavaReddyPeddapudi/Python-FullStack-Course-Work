'''
Syntax :

for var in seq:
 #statement

seq : list, tuple, set, dict, str,range
'''

products = {'bread','butter','milk','sugar','salt'}
for item in products:
    print(item)
print('\n')


products = {'bread':30,'butter':50,'milk':20,'sugar':45,'salt':60}
for items in products:
    print("Product name : ",items)
    print("Product price : ",products[items])
    print("Buy Now | Add to cart ")
    print("Add to fav ")
    print('---------------------------------------------------------')

print('\n')

s=('PYTHON PROGRAMMING ')
for ch in s:
    print(ch)

for i in range(2,100,2):
    print(i)
for i in range(10,1,-1):
    print(i)

n=int(input("Enter the number : "))
for i in range(1,21):
    print(f'{n}*{i}={n*i}')

print('\n Break statement ')
for i in range(10):
    if i ==4:
        break
    print(i)
print('\n')
print(' Contine statement ')
for i in range(10):
    if i == 6:
        continue
    print(i)
    
pin=1234
for i in range(5):
    user_pin=int(input("Enter the pin : "))
    if user_pin == pin:
        print(" Login Successfull ")
        break
    else:
        print(" invalid pin try Again ")
else:
    print(" you have reached the max attempts, try again after 5 min ")
