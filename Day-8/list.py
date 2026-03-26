Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.

= RESTART: C:/Users/Adikesava Reddy/OneDrive/Desktop/CODEGNAN/PFS COURSE WORK/Day-8/function.py
5
6
Addition : 11
Subraction :  -1
Multiplication : 30
Division : 0.8333333333333334
Modulus : 5

Enter expression: 3-6
-3
a=[4,6,7,7]
b=[5,6,4,5]
a+b
[4, 6, 7, 7, 5, 6, 4, 5]
names=['raju','ramu','adi','bargav','gowtham']
len(names)
5
names[2]
'adi'
names[:2]
['raju', 'ramu']
names[2:]
['adi', 'bargav', 'gowtham']
names[1:3]
['ramu', 'adi']
names[:-2]
['raju', 'ramu', 'adi']
names[-3]
'adi'
'adi' in names
True
'ajay' in names
False
a,b,c,d,e=names
a
'raju'
b
'ramu'
c
'adi'
d
'bargav'
e
'gowtham'
names
['raju', 'ramu', 'adi', 'bargav', 'gowtham']
id(names)
2010043413184
id(a)
2007901230864
id(a,b,c,d)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    id(a,b,c,d)
TypeError: id() takes exactly one argument (4 given)
>>> names.append('ashok')
>>> names
['raju', 'ramu', 'adi', 'bargav', 'gowtham', 'ashok']
>>> names.extend('a','b','c')
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    names.extend('a','b','c')
TypeError: list.extend() takes exactly one argument (3 given)
>>> names.extend(['a','b','c'])
>>> names
['raju', 'ramu', 'adi', 'bargav', 'gowtham', 'ashok', 'a', 'b', 'c']
>>> len(names)
9
>>> names.insert(1,'prasad')
>>> names
['raju', 'prasad', 'ramu', 'adi', 'bargav', 'gowtham', 'ashok', 'a', 'b', 'c']
>>> names.pop(2)
'ramu'
>>> names
['raju', 'prasad', 'adi', 'bargav', 'gowtham', 'ashok', 'a', 'b', 'c']
>>> del names(a)
SyntaxError: cannot delete function call
>>> del names('a')
SyntaxError: cannot delete function call
>>> sorted(names)
['a', 'adi', 'ashok', 'b', 'bargav', 'c', 'gowtham', 'prasad', 'raju']
>>> names.sort(1)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    names.sort(1)
TypeError: sort() takes no positional arguments
>>> l=sorted(names)
>>> l
['a', 'adi', 'ashok', 'b', 'bargav', 'c', 'gowtham', 'prasad', 'raju']
>>> l.reverse
<built-in method reverse of list object at 0x000001D3803DBC00>
>>> l.reverse()
>>> l
['raju', 'prasad', 'gowtham', 'c', 'bargav', 'b', 'ashok', 'adi', 'a']
