def calc_fact(n):
    if n <= 1:          # дъно на рекурсията
        return 1

    return n * calc_fact(n - 1)


n = int(input())

print(calc_fact(n))