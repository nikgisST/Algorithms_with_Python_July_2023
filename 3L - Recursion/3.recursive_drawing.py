def draw_figure(n):
    if n == 0:           # base case === дъно на рекурсията
        return

    print('*' * n)       # pre-action(before calling the recursion)
    draw_figure(n - 1)   # recursive call(step-in)                        след стигане на дъното, тогава чак от този ред се отива на долния
    print('#' * n)       # post-action(after returning from recursion)    ред, който се изпълнява след приключване на рекурсията


n = int(input())

draw_figure(n)