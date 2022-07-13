def calck_days(left, right, price, incomes):
    if right <= left:
        if incomes[left] >= price:
            return left+1
        else:
            return -1
    mid = (left + right) // 2
    if incomes[mid] >= price:
        return calck_days(left, mid, price, incomes)
    else:
        return calck_days(mid+1, right, price, incomes)


if __name__ == "__main__":
    days = int(input())
    incomes = list(map(int, input().split()))
    price = int(input())
    res = [calck_days(0, days - 1, price, incomes), calck_days(0, days - 1, price * 2, incomes)]
    print(*res, sep=' ')
