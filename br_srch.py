def broken_search(nums, target) -> int:
    def binary_search(array, in_target, left, right):
        mid = (left + right) // 2
        if array[mid] == in_target:
            return mid

        if right <= left:
            return -1

        if array[left] < in_target < array[mid]:
            return binary_search(array, in_target, left, mid)
        else:
            return binary_search(array, in_target, mid + 1, right)

    index = binary_search(nums, target, left=0, right=len(nums)-1)
    return index
