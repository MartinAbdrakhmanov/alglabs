def exponential_filter(values, alpha):
    filtered_values = [values[0]]
    for i in range(1, len(values)):
        filtered_values.append(
            alpha * values[i] + (1 - alpha) * filtered_values[-1])
    print(filtered_values)


if __name__ == '__main__':
    exponential_filter([1, 2, 3, 4, 5, 6, ], 0.5)
