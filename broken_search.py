def broken_search(nums, target) -> int:
    def binary_search(array, in_target, left, right):
        mid = (left + right) // 2
        if array[mid] == in_target:
            return mid

        if right <= left:
            return -1
        
        if array[mid] <= array[right]:
            if array[mid] < target <= array[right]:
                return binary_search(array, in_target, mid + 1, right) #right
            else:
                return binary_search(array, in_target, left, mid) #left
        else:
            if array[left] <= target < array[mid]:
                return binary_search(array, in_target, left, mid) #left
            else:
                return binary_search(array, in_target, mid + 1, right) #right

    index = binary_search(nums, target, left=0, right=len(nums)-1)
    return index


if __name__ == '__main__':
    length = int(input())
    trgt = int(input())
    arr = list(map(int, input().split()))
    
    print (broken_search (arr, trgt))
