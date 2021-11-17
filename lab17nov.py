for i in range(8):
    print(i)

print('-----------')
for i in range(3, 7):
    print(i)

print('-----------')
for i in range(8):
    if i == 3:
        continue
    if i == 6:
        break
    print(i)


def sum(a, b):
    print('a=%s' % a)
    print('b=%s' % b)
    a = 100
    return a + b


a = 10
b = 20
