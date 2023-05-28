def is_valid(board, row, column):
    # проверяем, лежит ли новый ферзь в прямой линии или на диагонали с другими ферзями
    for i in range(row):
        if board[i] == column or \
                board[i] - i == column - row or \
                board[i] + i == column + row:
            return False
    return True


def n_queens(board, row):
    n = len(board)
    if row == n:
        # если все 8 строк заполнены - нашли доску с корректной расстановкой ферзей
        print(board)
    else:
        # перебираем все варианты расстановки ферзя на текущей строке
        for i in range(n):
            if is_valid(board, row, i):
                board[row] = i
                n_queens(board, row + 1)


board = [0] * 8
if __name__ == '__main__':
    n_queens(board, 0)
