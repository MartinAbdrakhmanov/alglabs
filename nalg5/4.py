def count_ways(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    if n == 2:
        return 2

    steps = [0] * n
    steps[0] = 1
    steps[1] = 1
    steps[2] = 2

    for i in range(3, n):
        steps[i] = steps[i - 1] + steps[i - 2] + steps[i - 3]

    return steps[n - 1] + steps[n - 2] + steps[n - 3]


if __name__ == "__main__":
    print(count_ways(int(input('Введите количество ступенек: '))))
