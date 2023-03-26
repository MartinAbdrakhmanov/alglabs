def change():
    n = int(input('Change: '))
    m1 = int(input('Coin1: '))
    s1 = int(input('Quantity: '))
    m2 = int(input('Coin2: '))
    s2 = int(input('Quantity: '))
    m3 = int(input('Coin3: '))
    s3 = int(input('Quantity: '))
    m4 = int(input('Coin4: '))
    s4 = int(input('Quantity: '))
    cash = {m1: s1, m2: s2, m3: s3, m4: s4}
    sm = m1*s1 + m2*s2 + m3*s3 + m4*s4
    if sm < n:
        return ('Not possible :(')
    cash = dict(sorted(cash.items(), reverse=True))
    changedict = dict(
        sorted({m1: 0, m2: 0, m3: 0, m4: 0}.items(), reverse=True))
    for i in cash.keys():
        if n > i*cash[i]:
            n -= i*cash[i]
            changedict[i] += cash[i]
        else:
            changedict[i] += n//i
            n -= (n//i)*i
    return changedict, n


if __name__ == '__main__':
    dct, n = change()
    print(dct, 'Remaining:', n)
