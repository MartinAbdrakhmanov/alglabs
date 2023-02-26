
import timeit


def fnd(s, sb):
    s = s[::-1]
    for i in range(len(s)):
        if s[i] == sb:
            return i
    return False


def bm(s, h):
    ls = len(s)
    i = ls
    cnt = 0
    while i <= len(h):
        step = 0
        for j in range(ls):
            if h[i-j-1] != s[ls-j-1]:
                tmp = fnd(s, h[i-j-1])
                if tmp:
                    i += tmp
                    break
                else:
                    i += ls - step
                    break
            elif j == ls-1:
                cnt += 1
                i += 1
            else:
                step += 1
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
    k = bm(s, h)
    if mx < k:
        mx = k
        b = s
print(mx, b)
print("Время работы: ", end='')
print(timeit.default_timer() - start_time)
