a = int(input('введите 1 число'))
b = int(input('введите 2 число'))
c = int(input('введите 3 число'))

if a <= b and a <= c:
    m = a
elif b <= a and b <= c:
    m = b
else:
    m = c

print(f'минимум равен {m}')
