def find_zero(arr):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] >= arr[high]:
            low = mid + 1
        else:
            high = mid
    return high if high else len(arr) - 1

def broken_search(nums, target) -> int:
    def binarySearch(array, in_target, left, right):
        mid = (left + right) // 2
        print("Mid: " + str(mid) + " = " + str(array[mid]))
        if array[mid] == in_target:
            return mid

        if right <= left:
            return -1
        if in_target < array[mid]:
            print(str(in_target) + "<" + str(array[mid]))
            if in_target >= array[left]:
                print("Going left as got True: " + str(in_target) + ">=" + str(array[left]))
                return binarySearch(array, in_target, left, mid)
            else:
                print("Going right as got False: " + str(in_target) + ">=" + str(array[left]))
                return binarySearch(array, in_target, mid + 1, right)
        else:
            print("Going right as got False: " + str(in_target) + "<" + str(array[mid]))
            return binarySearch(array, in_target, mid + 1, right)


    index = binarySearch(nums, target, left=0, right=len(nums)-1)
    return index


if __name__ == '__main__':
    ln = int(input())
    k = int(input())
    arr = [int(x) for x in input().split(' ')]
    print ("Target = " + str(k))
    print(find_zero(arr))


'''
тест дата:

9
7
12 14 17 19 22 33 7 10 11

 
'''