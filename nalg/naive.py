
def naive(ndl, hay):
    i = 0
    ln = len(ndl)
    s = 0
    for i in range(len(hay) - ln + 1):
        for j in range(ln):
            if ndl[j] != hay[i+j]:
                i += 1
                break
            elif j == ln-1:
                s += 1
    return s


a = [0, 1]
for i in range(498):
    a.append(a[i] + a[i+1])
h = ''.join(map(str, a))
mx = -1
b = ''
for i in range(10, 100):
    s = str(i)
    # mx = max(mx, kmp(s, h))
    k = naive(s, h)
    if mx < k:
        mx = k
        b = s
print(f'Чаще всего встречается число - {b}, {mx} раз')
