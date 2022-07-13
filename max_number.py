import functools

def mycmp(a, b):
    return -1 if (a[0] * 10 ** len(b[1]) + b[0]) > (b[0] * 10 ** len(a[1]) + a[0]) else 1


def calc_max_number(num_count, nums):
    nums = sorted(nums, key=functools.cmp_to_key(mycmp))
    return ''.join([x[1] for x in nums])


if __name__ == "__main__":
    count = int(input())
    numbers = [tuple([int(x), x]) for x in input().split(' ')]
    print(calc_max_number(count - 1, numbers))