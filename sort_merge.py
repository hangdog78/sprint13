def merge_sort(array, lf, rf):
    if rf - lf <= 1:
        return
    mid = (lf + rf) // 2
    merge_sort(array, lf, mid)
    merge_sort(array, mid, rf)
    array[lf:rf] = merge(array, lf, mid, rf)


def merge(arr, lf, mid, rf):

    first = arr[lf: mid]
    second = arr[mid: rf]

    if not first:
        return second
    if not second:
        return first

    result = []
    l, r = 0, 0
    while l < len(first) and r < len(second):
        # выбираем, из какого массива забрать минимальный элемент
        if first[l] <= second[r]:
            result += [first[l]]
            l += 1
        else:
            result += [second[r]]
            r += 1

    while l < len(first):
        result += [first[l]]  # перенеси оставшиеся элементы left в result
        l += 1
    while r < len(second):
        result += [second[r]]  # перенеси оставшиеся элементы right в result
        r += 1

    return result
