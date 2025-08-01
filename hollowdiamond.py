n = 5  # Height of diamond (half), change as needed

# Upper part
for i in range(1, n + 1):
    print(' ' * (n - i), end='')
    if i == 1:
        print('*')
    else:
        print('*' + ' ' * (2 * i - 3) + '*')

# Lower part
for i in range(n - 1, 0, -1):
    print(' ' * (n - i), end='')
    if i == 1:
        print('*')
    else:
        print('*' + ' ' * (2 * i - 3) + '*')