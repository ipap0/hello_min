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

if a <= b and a <= c:
    m = a
if b <= a and b <= c:
    m = b
if c <= a and c <= b:
    m = c

print(f'минимум равен {m}')

if a <= b:
    if a <= c:
        m = a
    else:
        m = c
else:
    if b <= c:
        m = b
    else:
        m = c
print(f'минимум равен {m}')

m = a
if b < m:
    m = b
if c < m:
    m = c
print(f'минимум равен {m}')