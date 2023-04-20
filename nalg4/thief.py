def heist():
    n = int(input('N of exhibits: '))
    m = int(input('rounds: '))
    k = int(input('weight per round: '))

    pw = [[0, 0]]
    for e in range(n):
        print(f'price and weight of {e+1} exhibit:')
        info = list(map(int, input().split()))
        pw.append(info)
    pw = sorted(pw, key=lambda x: (x[1], x[0]))
    stolen = []
    stolenm = 0
    t = [[-1 for _ in range(k+1)] for _ in range(n+1)]
    for _ in range(m):
        for i in range(n+1):
            for w in range(k+1):
                if i == 0 or w == 0:
                    t[i][w] = 0
                elif (pw[i][1] <= w):
                    t[i][w] = max(pw[i][0]+t[i-1][w-pw[i][1]], t[i-1][w])
                else:
                    t[i][w] = t[i-1][w]

        while i > 0 and w > 0:
            if (t[i][w] == t[i-1][w]):
                i -= 1
            else:
                pwc = pw[i].copy()
                stolen.append(pwc)
                stolenm += pwc[0]
                w -= pw[i][1]
                pw[i][1] = float('inf')
                i -= 1
    print(
        f'Those artifacts were stolen: {stolen}. Approximate losses are over {stolenm} million$')


if __name__ == '__main__':
    heist()
