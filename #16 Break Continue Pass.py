
x = int(input('How Many Chocolates You Want?'))

i = 1
while i <= x:
    print("Chocolates")
    i += 1

av = 6
x = int(input('how many Chocolates you Want to purchase?'))
i = 1
while i <= x:

    if i>av:
        print('out of stock')
        break


    print('purchased chocolate')
    i += 1

print('Good Bye')


for i in range(1,101):
    if i%3==0 or i%5==0:
        continue

    print(i)


print("Bye")

for i in range(1,101):
    if i%2!=0:
        pass
    else:
        print(i)