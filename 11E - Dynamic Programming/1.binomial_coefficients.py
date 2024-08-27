def calc_binom(n, k, memo):    # with dynamic programming Memoization  save/cache sub-problem solutions for later use
    key = f'{n} {k}'   # създаваме ключ от двата индекса на конкретна стойност:  4 3
    if key in memo:
        return memo[key]

    if n == 0 or k == 0 or n == k:
        return 1

    result = calc_binom(n - 1, k - 1, memo) + calc_binom(n - 1, k, memo)   # преди да върнем този резултат от рекурсията, искаме да го запазим в речника
    memo[key] = result   # добавяме в речника този съответния образуван ключ с неговия резултат
    return result


n = int(input())   # row
k = int(input())   # col
print(calc_binom(n, k, {}))


####################################################################

def calc_binom(n, k):      # with recursion
    if n == 0 or k == 0 or n == k:
        return 1
    return calc_binom(n - 1, k - 1) + calc_binom(n - 1, k)

n = int(input())
k = int(input())
print(calc_binom(n, k))
