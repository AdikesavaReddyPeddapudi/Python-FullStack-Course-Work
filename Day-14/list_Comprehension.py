
print("List comprehension examples: \n")
a=[]
for i in range(1,11):
    a.append(i)
print("a:", a)

a=[i for i in range(1,11)]
print("Numbers from 1 to 10:", a)

for i in range(1,11):
    if i%2==0:
        a.append(i)
print("Even numbers from 1 to 10:", a)

a=[i for i in range(1,100) if i%2==0]
print("Even numbers from 1 to 99:", a)

a=[i**2 for i in range(1,11)]
print("Squares of numbers from 1 to 10:", a)

a=[i**3 for i in range(1,11)]
print("Cubes of numbers from 1 to 10:", a)

a=[i for i in range(0,101,3)]
print("Multiples of 3 from 0 to 100:", a)

s='python programming'
vowels='aeiouAEIOU'

a=[' * ' if i in vowels else i for i in s]
print("String with vowels replaced by '*': ", a)

l=[4,5,3,7,8,4,3,34,45,23,56,78,90,12]
a=[0 if i%2==0 else i for i in l]
print("List with even numbers replaced by '0': ", a)




print("Dictionary comprehension: \n")

l=[4,6,4,2,6,8,9,6,5,3,7,9,5,4,3,2,1,0]

r1={i for i in range(1,11)}
print("Dictionary object: ", r1)

r1={i : l.count(i) for i in l}
print("Dictionary object: ", r1)

print("Set comprehension: \n")
r1={i for i in range(1,11)}
print("Set object: ", r1)

r1={i : l.count(i) for i in l}
print("Set object: ", r1)

r1={i for i in l}
print("Set object: ", r1)



from ast import pattern


print("Generator comprehension: \n")

def reels():
    r=['1..100','101..200','201..300','301..400','401..500','501..600','601..700','701..800','801..900','901..1000']
    for i in r:
        yield i
g=reels()
print("Generator object: ", next(g))
print("Generator object: ", next(g))
print("Generator object: ", next(g))
print("Generator object: ", next(g))
print("Generator object: ", next(g))
print("Generator object: ", next(g))
print("Generator object: ", next(g))
print("Generator object: ", next(g))
print("Generator object: ", next(g))
print("Generator object: ", next(g))

squared = (x**2 for x in range(5))
for num in squared:
    print("squared num:", num)


def display():
    for i in range(1,6):
        yield i**2
squares = display()
for square in squares:
    print("Square:", square)

def pattern(n):
    for i in range(1, n + 1):
        print('* ' * i)
    for i in range(n - 1, 0, -1):
        print('* ' * i)
pattern(5)

# inverse triangle pattern
def pattern(n):
    for i in range(n, 0, -1):
        for j in range(n - i):
            print(' ', end='')
        print('* ' * i)
pattern(5)

# diamond pattern

def pattern(n):
    for i in range(1, n + 1):
        print(' ' * (n - i) + '* ' * i)
    for i in range(n - 1, 0, -1):
        print(' ' * (n - i) + '* ' * i)
pattern(10)

# list,map,filter
l=[1,2,3,4,5,6,7,8,9,10]

print("map: \n")
squared = list(map(lambda x: x**2, l))
print("Squared numbers using map:", squared)
squared = [x**2 for x in l]
print("Squared numbers using list comprehension:", squared)

print("\n filter: \n")
even_numbers = list(filter(lambda x: x % 2 == 0, l))
print("Even numbers using filter:", even_numbers)
even_numbers = [x for x in l if x % 2 == 0]
print("Even numbers using list comprehension:", even_numbers)