Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
d={}
type(d)
<class 'dict'>
d=dict()
d
{}
data={'name':'adi','age':23,'course':'pfs','skills':['puthon','sql','plsql']}
data
{'name': 'adi', 'age': 23, 'course': 'pfs', 'skills': ['puthon', 'sql', 'plsql']}
d
{}
data['name']
'adi'
data['age']
23

data['skills']
     
['puthon', 'sql', 'plsql']
d=data
     
d
     
{'name': 'adi', 'age': 23, 'course': 'pfs', 'skills': ['puthon', 'sql', 'plsql']}
data
     
{'name': 'adi', 'age': 23, 'course': 'pfs', 'skills': ['puthon', 'sql', 'plsql']}
d[1]='int'
     
d
     
{'name': 'adi', 'age': 23, 'course': 'pfs', 'skills': ['puthon', 'sql', 'plsql'], 1: 'int'}

d[3+6j]='complex'
     
d
     
{'name': 'adi', 'age': 23, 'course': 'pfs', 'skills': ['puthon', 'sql', 'plsql'], 1: 'int', (3+6j): 'complex'}
d[True]='boolean'
     
d
     
{'name': 'adi', 'age': 23, 'course': 'pfs', 'skills': ['puthon', 'sql', 'plsql'], 1: 'boolean', (3+6j): 'complex'}
id(d)
     
2621256092608
d[9]='adikesava'
     
d
     
{'name': 'adi', 'age': 23, 'course': 'pfs', 'skills': ['puthon', 'sql', 'plsql'], 1: 'boolean', (3+6j): 'complex', 9: 'adikesava'}
id(d)
     
2621256092608
d['name']
     
'adi'
d['name']='Adikesava'
     
d
     
{'name': 'Adikesava', 'age': 23, 'course': 'pfs', 'skills': ['puthon', 'sql', 'plsql'], 1: 'boolean', (3+6j): 'complex', 9: 'adikesava'}
d.items()
     
dict_items([('name', 'Adikesava'), ('age', 23), ('course', 'pfs'), ('skills', ['puthon', 'sql', 'plsql']), (1, 'boolean'), ((3+6j), 'complex'), (9, 'adikesava')])
d.keys()
     
dict_keys(['name', 'age', 'course', 'skills', 1, (3+6j), 9])
d.values()
     
dict_values(['Adikesava', 23, 'pfs', ['puthon', 'sql', 'plsql'], 'boolean', 'complex', 'adikesava'])
d.update({9:'Vikram'})
     
d
     
{'name': 'Adikesava', 'age': 23, 'course': 'pfs', 'skills': ['puthon', 'sql', 'plsql'], 1: 'boolean', (3+6j): 'complex', 9: 'Vikram'}

>>> d.popitem()
...      
(9, 'Vikram')


>>> data.popitem()
...      
((3+6j), 'complex')
>>> data
...      
{'name': 'Adikesava', 'age': 23, 'course': 'pfs', 'skills': ['puthon', 'sql', 'plsql'], 1: 'boolean'}
>>> d.pop(1)
...      
'boolean'
>>> d
...      
{'name': 'Adikesava', 'age': 23, 'course': 'pfs', 'skills': ['puthon', 'sql', 'plsql']}
>>> data
...      
{'name': 'Adikesava', 'age': 23, 'course': 'pfs', 'skills': ['puthon', 'sql', 'plsql']}
>>> data.clear()
...      
>>> data
...      
{}
