
# бинарный поиск по строчкам матрицы
def finder(row, n):
    left = 0
    right = len(row)
    if row[right-1] < n or row[left] > n:
        return -1
    while right > left:
        mid = (left+right)//2
        if row[mid] == n:
            return mid
        elif row[mid] < n:
            left = mid+1
        else:
            right = mid
    return -1


def findmatrix(matrix, n):
    for i in range(len(matrix)):
        res = finder(matrix[i], n)
        if res != -1:
            print(f'Element {n} is in row {i+1}, col {res+1}')


if __name__ == '__main__':
    matrix = [[1, 2, 3],
              [3, 4, 5]]
    print(*matrix, sep='\n')
    findmatrix(matrix, 4)
