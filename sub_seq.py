def is_subsequence(s, t):
    lens, lent = len(s), len(t)
    if lens > lent:
        return False

    i = 0
    for j in range(lent):
        if s[i] == t[j]:
            i += 1
            if i == lens:
                return True

    return False


if __name__ == "__main__":
    s = input()
    t = input()
    print(is_subsequence(s, t), end='')
