from random import randint


def xd():
    n = int(input('N is equal to: '))
    a = [randint(-100, 100) for _ in range(n)]
    mxlen = 0
    currlen = 1
    mxseq = []
    currseq = [a[0]]
    for i in range(1, n):
        if a[i] > a[i-1]:
            currlen += 1
            currseq.append(a[i])
            if currlen > mxlen:
                mxlen = currlen
                mxseq = currseq
        else:
            currlen = 1
            currseq = [a[i]]
    print('Initial Array: ', a)
    print(f'Max len is: {mxlen}')
    print(f'Longest sequence is: {mxseq}')


if __name__ == '__main__':
    xd()
