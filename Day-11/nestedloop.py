n=int(input("Enter the Size : "))

for i in range(n): # rows
    for j in range(n):  #columuns
        print('*',end=' ')
    print()

print()
for i in range(n+1): # rows
    for j in range(n):  #columuns
        print(i,end=' ')
    print()

print()
for i in range(0,n):
    for j in range(0,n+1):
        print(j,end=' ')
    print()
    
print()

for i in range(0,n):
   for j in range(0,n):
       print((i+j)%2,end=' ')
   print()

print()

for i in range(n+1):
    for j in range(i):
        print('*',end=' ')
    print()
print()

for i in range(n):
    for j in range(n-i):
        print('*',end=' ')
    print()
print()

for i in range(n):
    for s in range(n-i-1):
        print(' ',end=' ')
    for j in range(i+1):
        print('*',end=' ')
    print()

for i in range(n):
    for s in range(i):
        print(' ',end=' ')
    for j in range(n-i):
        print('*',end=' ')
    print()


for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1 or i==n//2 or j==n//2:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()


for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j+i==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

   
for i in range(n):
    for j in range(n):
        if   j+i==n-1 or i==j:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()