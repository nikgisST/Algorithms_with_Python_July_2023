def iterative_fib(number):
    fib0 = 1
    fib1 = 1
    result = 0
    for _ in range(number - 1):
        result = fib0 + fib1
        fib0, fib1 = fib1, result
    return result

n = int(input())
print(iterative_fib(n))



#################################################


def iterative_fib(number):
    if number <= 2:
        return 1
    return iterative_fib(number - 1) + iterative_fib(number - 2)

n = int(input())
print(iterative_fib(n))