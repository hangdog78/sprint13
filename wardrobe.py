def counting_sort(array, k):
    counted_values = [0] * k
    for value in array:
        counted_values[value] += 1

    index = 0
    for value in range(0, k):
        for amount in range(0, counted_values[value]):
            array[index] = value
            index += 1

    return array


if __name__ == "__main__":
    days = int(input())
    incomes = list(map(int, input().split()))
    print(*counting_sort(incomes, 3), sep=' ')
