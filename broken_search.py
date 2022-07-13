
def broken_search(nums, target) -> int:
    if len(nums) == 1:
        return -1

    mid = len(nums)//2
    left = nums[0:mid]


def test():
    arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
    assert broken_search(arr, 5) == 6
