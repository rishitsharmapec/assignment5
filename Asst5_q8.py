list_nums = []
for i in range(10):
    num = int(input('Enter a number: '))
    list_nums.append(num)
# Positive numbers
print('Positive numbers: ', end='')
for i in list_nums:
    if i >= 0:
        print(i, end=' ')
print()

# Negative numbers
print('Negative numbers: ', end='')
for i in list_nums:
    if i < 0:
        print(i, end=' ')
print()

# Odd numbers
print('Odd numbers: ', end='')
for i in list_nums:
    if i % 2 != 0:
        print(i, end=' ')
print()

# Even numbers
print('Even numbers: ', end='')
for i in list_nums:
    if i % 2 == 0:
        print(i, end=' ')
print()

# Number of times each number occurs in the List
for i in list_nums:
    print(f'{i} occurs {list_nums.count(i)} times in the list')