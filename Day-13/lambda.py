

wish=lambda name: f"hello {name}"

print(wish("Alice"))
print(wish("Bob"))


add=lambda x,y: x+y
print("Addition : ", add(5, 3))
print("Addition : ", add(10, 20))  

add=lambda x,y,z:x+y+z
print("Addition : ", add(5, 3, 2))

avg=lambda a,b,c : (a+b+c)/3
print("Average : ",avg(10,20,30))
print("Average : ",avg(5,15,25))

num=lambda e: "even" if e%2==0 else "odd"
print("Number is : ", num(4))
print("Number is : ", num(7))

iseven = lambda n: "even" if n % 2 == 0 else "odd"
print("Number is : ", iseven(4))
print("Number is : ", iseven(7))    

isodd = lambda n: "odd" if n%2==1 else "even"
print("Number is : ", isodd(4))
print("Number is : ", isodd(7))    

greater=lambda x,y:x if x>y else y
print("Greater number is : ", greater(5,8))

vowels='aeiouAEIOU'
isvowel=lambda v:"vowel" if v in vowels else "consonants"
print("Character is : ", isvowel('a'))
print("Character is : ", isvowel('b'))

l=[10,20,30,40,50]
res=list(map(lambda x:x+10,l))
print("Doubled list : ", res)

per=list(map(lambda x:x+x*0.18,l))
print("GST : ", per)

arr=['anju','prasad','suresh','raju']
res=list(map(lambda i:i.title(),arr))
print("Title case : ", res)
res=list(map(lambda i:i.upper(),arr))
print("Upper case : ", res)
res=list(map(lambda i:i.lower(),arr))
print("Lower case : ", res)



L=[1,2,3,4,5,6,7,8,9,10]
res=list(filter(lambda x:x%3==0,L))
print('Divisible numbers: ', res)

l=[10,20,30,40,50,60,70,80,90,100]
res=list(filter(lambda x:x>60,l))
print('Numbers greater than 60: ', res)



l={'laptop':True,
   'mobile':False,
   'tablet':True,
   'desktop':False,
   'charger':True
   }

res=list(filter(lambda x:l[x],l))
print('Available items: ', res)



randomnum=[3,54,7,5,2,1,4,6,7,65,34,2,1,56,8,9,0]
randomnum.sort()
res=list(filter(lambda x: x % 2 == 0 and x!=0, randomnum))
print('Even numbers: ', res)
res=list(filter(lambda x : x %2 ==1, randomnum))
print('odd numbers: ', res)



from functools import reduce
l=[3,54,7,5,2,1,4,6,7,65,34,2,1,56,8,9]
res=reduce(lambda x,y:x+y,l)
print("Sum of list : ", res)
res=reduce(lambda x,y:x*y,l)
print("Product of list : ", res)

L=['python','java','c++','javascript']
res=reduce(lambda x,y:x+" "+y,L)
print("Concatenated string : ", res)



data={
    'apple': 50,
    'banana': 80,
    'orange': 60,
    'grape': 40,
    'mango': 70
}
print(dict(sorted(data.items(),key=lambda x:x[1])))
print(dict(sorted(data.items(),key=lambda x:x[1],reverse=True)))