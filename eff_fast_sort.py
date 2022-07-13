# Успешная версия: 69386292
import random


class Student:
    def __init__(self, name, tasks, penalties):
        self.name = name
        self.tasks = int(tasks)
        self.penalties = int(penalties)

    def __lt__(self, other):
        if self.tasks == other.tasks:
            if self.penalties == other.penalties:
                return self.name < other.name
            return self.penalties < other.penalties
        return self.tasks > other.tasks

    def __str__(self) -> str:
        return self.name


def quicksort(nums, fst, lst):
    if fst >= lst:
        return

    i, j = fst, lst
    pivot = nums[random.randint(fst, lst)]

    while i <= j:
        while nums[i] < pivot:
            i += 1
        while nums[j] > pivot:
            j -= 1
        if i <= j:
            nums[i], nums[j] = nums[j], nums[i]
            i, j = i + 1, j - 1
    quicksort(nums, fst, j)
    quicksort(nums, i, lst)


if __name__ == '__main__':
    length = int(input())
    students = []
    for _ in range(0, length):
        students += [Student(*input().split())]

    quicksort(students, 0, length-1)
    print(*students, sep='\n')
