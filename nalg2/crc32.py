def crc(a):
    g = '100000' + bin(int('04C11DB7', 16))[2:]
    st = ''
    for i in a:
        st += bin(ord(i))[2:]
    st += '0'*32
    st = list(map(int, st))
    g = list(map(int, g))
    step = 0
    while len(g) <= len(st[step:]):
        if st[step] == 0:
            step += 1
            continue
        else:
            for i in range(33):
                st[i+step] = st[i+step] ^ g[i]
            step += 1
    return st[-32:]


if __name__ == '__main__':
    a = input()
    print('hash:', hex(int(''.join(map(str, crc(a))), 2))[2:])
