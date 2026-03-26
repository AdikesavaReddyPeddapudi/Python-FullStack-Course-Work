
def arithmetic(a,b):
    add=a+b
    sub=a-b
    mul=a*b
    div=a/b
    mod=a%b
    print("Addition :",add)
    print("Subraction : ",sub)
    print("Multiplication :",mul)
    print("Division :",div)
    print("Modulus :",mod)
a=int(input())
b=int(input())
arithmetic(a,b)

print()

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

exp = input("Enter expression: ") 

if '+' in exp:
    a,b = exp.split('+')
    print(add(int(a),int(b)))

elif '-' in exp:
    a,b = exp.split('-')
    print(sub(int(a),int(b)))

elif '*' in exp:
    a,b = exp.split('*')
    print(mul(int(a),int(b)))

elif '/' in exp:
    a,b = exp.split('/')
    print(div(int(a),int(b)))

