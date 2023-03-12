def divhash(a):
    m = len(a)
    na = []
    hash = ''
    for i in range(m):
        na.append(ord(a[i]))
    for j in range(m):
        hash += str(hex(na[j] % m))[2:]
    return hash


if __name__ == '__main__':
    a = input()
    print('hash:', divhash(a))
