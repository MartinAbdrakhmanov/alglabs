
def hash(st, ls, a):
    a = list(a)
    ln = len(a)
    s = 0
    for i in range(ls+1):
        s += a.index(st[i])*ln**(ls-i)
    return s


def rabinkarp(s, h):
    a = []
    sm = 0

    for i in range(len(h)):

        if not (h[i] in a):
            a.append(h[i])
    hs = hash(s, len(s)-1, a)
    for i in range(len(h) - len(s) + 1):

        if hash(h[i:i+len(s)], len(h[i:i+len(s)])-1, a) == hs:
            sm += 1
    return sm


a = [0, 1]
for i in range(498):
    a.append(a[i] + a[i+1])
h = ''.join(map(str, a))
mx = -1
b = ''
for i in range(10, 100):
    s = str(i)

    k = rabinkarp(s, h)
    if mx < k:
        mx = k
        b = s
print(f'Чаще всего встречается число - {b}, {mx} раз')
