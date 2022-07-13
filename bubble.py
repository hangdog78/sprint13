def bubble_sort(nums):
    is_sorted = True
    for j in range(0, len(nums)-1):
        swaps = False
        for i in range(0, len(nums)-1):
            if nums[i] > nums[i+1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swaps = True
                is_sorted = False
        if swaps == False:
            break
        print(*nums)
    if is_sorted:
        print(*nums)


if __name__ == '__main__':
    length = int(input())
    arr = list(map(int, input().split()))
    bubble_sort(arr)
