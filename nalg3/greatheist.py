def heist():
    n = int(input('N of exhibits: '))
    m = int(input('rounds: '))
    k = int(input('weight per round: '))
    exhibition = []
    for e in range(n):
        print(f'price and weight of {e+1} exhibit:')
        info = list(map(int, input().split()))
        exhibition.append(info)
    exhibition = sorted(exhibition, key=lambda x: (x[0], -x[1]), reverse=True)

    stolen = 0
    for i in range(m):
        currweight = 0
        for j in range(i, n):
            if currweight + exhibition[j][1] > k:
                continue
            else:
                currweight += exhibition[j][1]
                stolen += exhibition[j][0]
                exhibition[j][1] = 0
                exhibition[j][0] = 0
    return stolen


if __name__ == '__main__':
    print('Stolen:', heist())
