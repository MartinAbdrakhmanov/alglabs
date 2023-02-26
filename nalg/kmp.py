
import timeit


def prefix(s):
    mx = 0
    s1 = ''
    s2 = ''
    for i in range(len(s)//2):
        s1 += s[i]
        s2 = s[len(s)-i-1] + s2
        if s1 == s2:
            mx = i+1
    return mx


def kmp(s, h):
    pr = [0]
    for i in range(len(s)):
        pr.append(prefix(s[:i+1]))

    h = ' ' + h
    s = ' ' + s
    j = 0
    i = 1
    cnt = 0
    while i < len(h):
        if h[i] == s[j+1]:
            if j+1 == len(s)-1:
                cnt += 1
                j = 0
                i += 1
            else:
                j += 1
                i += 1
        elif j != 0:
            j = pr[j]
        else:
            i += 1
    return cnt


start_time = timeit.default_timer()
a = [0, 1]
for i in range(498):
    a.append(a[i] + a[i+1])
h = ''.join(map(str, a))
mx = -1
b = ''
for i in range(10, 100):
    s = str(i)
    # mx = max(mx, kmp(s, h))
    k = kmp(s, h)
    if mx < k:
        mx = k
        b = s
print(mx, b)
print("Время работы: ", end='')
print(timeit.default_timer() - start_time)
