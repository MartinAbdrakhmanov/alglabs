import numpy as np


def check(ttt, tr=False):
    xwon = ['x', 'x', 'x']
    owon = ['o', 'o', 'o']
    if tr:
        ttt = list(np.transpose(ttt))
    for i in ttt:
        if tr:
            i = str(i).strip('[').strip(']').replace("'", '').split()
        if i == xwon:
            return 'x won'
        if i == owon:
            return 'o won'


def winner(ttt):
    p1 = check(ttt)
    if p1:
        return p1
    p2 = check(ttt, True)
    if p2:
        return p2
    for i in ['x', 'o']:
        if all(ttt[k][k] == i for k in range(3)) or all(ttt[k][2-k] == i for k in range(3)):
            return f'{i} won'
    return 'draw'


if __name__ == '__main__':

    ttt = [['x', 0, 'o'],
           ['x', 'o', 0],
           ['x', 'o', 'x']]
    # ttt = [['o', 'x', 'o'],
    #        ['x', 'x', 'o'],
    #        ['x', 'o', 'x']]
    print(winner(ttt))
