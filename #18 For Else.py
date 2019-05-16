nums = [12,15,18,21,26]

for num in nums:
    if num % 5 == 0:
        print(num)


nums = [12,16,18,20,25]

for num in nums:
    if num % 5 == 0:
        print(num)


nums = [2,3,5,6,8,9]

for num in nums:
    if num % 3 == 0:
        print(num)
        break


nums = [2,3,5,6,8,9]

for num in nums:
    if num % 7 == 0:
        break
else:
    print('not found')