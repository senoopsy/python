a = 9
b = 6

temp = a
a = b
b = temp

a = a + b   #15
b = a - b   #9
a = a - b   #6

a = a ^ b
b = a ^ b
a = a ^ b

a,b = b,a

print(a)
print(b)
