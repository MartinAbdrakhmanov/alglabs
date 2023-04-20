from random import randint


def chain():
    n = 26
    rows = [[3, 2], [2, 4], [4, 2], [2, 5], [5, 3], [3, 4], [4, 1], [1, 2], [2, 2], [2, 3], [3, 1], [1, 5], [5, 4], [4, 3],
            [3, 2], [2, 4], [4, 2], [2, 5], [5, 3], [3, 4], [4, 1], [1, 2], [2, 2], [2, 3], [3, 1], [1, 5]]
    # rows = [[3, 2], [2, 4], [4, 2], [2, 5]]
    global depth
    depth = [[] for _ in range(len(rows) + 1)]

    def order(i, j, kt, currd):
        if i == j:
            depth[currd].append(i)
            return
        order(i, kt[i][j], kt,  currd+1)
        order(kt[i][j]+1, j, kt, currd+1)

    d = []
    for i in range(len(rows)):
        d.append(rows[i][0])
    d.append(rows[-1][1])

    matrixes = [[[randint(1, 5) for _ in range(rows[j][1])]
                for _ in range(rows[j][0])] for j in range(len(rows))]
    c = [[float('inf') if i != j else 0 for j in range(len(rows)+1)]
         for i in range(len(rows)+1)]
    kt = [[0 for _ in range(len(rows)+1)] for _ in range(len(rows)+1)]

    for gap in range(1, len(rows)):
        for i in range(1, len(rows)):
            if i+gap < len(rows)+1:
                for k in range(i, i+gap):
                    currvalue = c[i][k] + c[k+1][i+gap] + \
                        d[i-1]*d[k]*d[i+gap]
                    if currvalue < c[i][i+gap]:
                        c[i][i+gap] = currvalue
                        kt[i][i+gap] = k

    order(1, len(rows), kt, 1)
    print('Best possible order:', end=' ')
    for i in depth[::-1]:
        for j in i:
            print(f'A{j}', end=' ')
    print('\nLeast amount of operations =', c[1][-1])


if __name__ == '__main__':
    chain()
