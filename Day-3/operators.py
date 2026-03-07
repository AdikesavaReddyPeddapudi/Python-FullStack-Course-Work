
print('Arithmetic Operator')
a = 10
b = 3
print(a + b) # Output: 13
print(a - b) # Output: 7
print(a * b) # Output: 30
print(a / b) # Output: 3.3333
print(a // b) # Output: 3
print(a % b) # Output: 1
print(a ** b) # Output: 1000

print('Comparison Operators')
x = 10
y = 5
print(x == y) # Output: False
print(x != y) # Output: True
print(x > y) # Output: True
print(x < y) # Output: False
print(x >= 10) # Output: True
print(y <= 5) # Output: True

print('Assignment Operators')
x = 10
x += 5 # x = x + 5 → 15
x *= 2 # x = x * 2 → 30
x -= 10 # x = x - 10 → 20
print(x) # Output: 20

print('Logical Operators')
x = 10
y = 20
print(x > 5 and y < 30) # Output: True (Both conditions are True)
print(x > 15 or y < 30) # Output: True (At least one condition is True)
print(not (x > 5)) # Output: False (Reverses the True condition)

print('Membership Operators')
fruits = ["apple", "banana", "cherry"]
print("apple" in fruits) # Output: True
print("grape" not in fruits) # Output: True

print('Identity Operators')
a = [1, 2, 3]
b = a
c = [1, 2, 3]
print(a is b) # Output: True (Both refer to the same object)
print(a is c) # Output: False (Different objects with the same content)
print(a is not c) # Output: True


print('Bitwise Operators')

x = 5 # Binary: 0101
y = 3 # Binary: 0011
print(x & y) # Output: 1 (Binary: 0001 → AND operation)
print(x | y) # Output: 7 (Binary: 0111 → OR operation)
print(x ^ y) # Output: 6 (Binary: 0110 → XOR operation)
print(~x) # Output: -6 (Binary: Inverts bits of 5)
print(x << 1) # Output: 10 (Binary: 1010 → Shifts left by 1)
print(x >> 1) # Output: 2 (Binary: 0010 → Shifts right by 1)


