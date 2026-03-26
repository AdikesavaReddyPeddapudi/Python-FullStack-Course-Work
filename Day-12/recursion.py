def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(5))  # Output: 120

print('\n-------------------------------------------------------------\n')

def display(n):
    if n > 10:
        return
    print(n)
    display(n + 1)
display(1)  # Output: 1 2 3 4 5 6 7 8 9 10

print('\n-------------------------------------------------------------\n')

def display_reverse(n):
    if n > 10:
        return
    display_reverse(n + 1)
    print(n)
display_reverse(1)  # Output: 10 9 8 7 6 5 4 3 2 1

print('\n-------------------------------------------------------------\n')

def display_string(s,i):
    if i == len(s):
        return
    print(s[:i+1])
    display_string(s, i + 1)
    print(s[:i+1])
display_string("Adikesava Reddy", 0)

print('\n-------------------------------------------------------------\n')

def display_rep(n,a):
    if a <= 0:
        return
    display_rep(n,a-1)
    print(n*a)
display_rep("Adikesava",5)

print('\n-------------------------------------------------------------\n')

def display_combi(s,i,n):
    if i ==len(s)-n:
        return
    print(s[i:i+n])
    display_combi(s,i+1,n)
display_combi("Adikesava",0,2)

print('\n-------------------------------------------------------------\n')

def display_sum(l,i,sum):
    if i==len(l):
        return sum
    return display_sum(l,i+1,sum+l[i])
print(display_sum([1,3,5,6,8],0,0))

print('\n-------------------------------------------------------------\n')

def dispaly_str_concat(l,i,sum):
    if i==len(l):
        return sum
    return dispaly_str_concat(l,i+1,sum+l[i])
print(dispaly_str_concat(["Adikesava","Reddy","Andhra Pradesh","India"],0,""))