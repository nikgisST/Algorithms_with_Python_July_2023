def find_all_paths(row, col, lab, direction, path):
    if row < 0 or col < 0 or row >= len(lab) or col >= len(lab[0]):  # граница, от която не трябва да излизаме, 
        return                                       # хваща невалидните координати и не ги пуска към рекурсиите долу
    if lab[row][col] == '*':
        return
    if lab[row][col] == 'visited_node':
        return

    path.append(direction)   # path = ['R', 'R', 'D', 'D', 'R']

    if lab[row][col] == 'e':         # ако сме стигнали до 'е', не трябва да правим повече рекурсивни извиквания
        print(''.join(path))         # и просто трябва да принтираме образуваната вече матрица
    else:
        lab[row][col] = 'visited_node'
        find_all_paths(row, col + 1, lab, 'R', path)    # денифира посока надясно
        find_all_paths(row, col - 1, lab, 'L', path)    # дефинира посока наляво
        find_all_paths(row + 1, col, lab, 'D', path)    # дефинира посока надолу
        find_all_paths(row - 1, col, lab, 'U', path)    # дефинира посока нагоре
        lab[row][col] = '-'   # замяна с този знак през пътя, по който сме минали === UNMAKE VISITED

    path.pop()     # post-action === back track - премахва последната добавена посока от списъка path, което означава, че се връщаме
                   # позволява на рекурсията да се върне назад и да проучи други възможни пътища, които не са били минавани досега

rows = int(input())
cols = int(input())
lab = []

for _ in range(rows):
    lab.append(list(input()))

find_all_paths(0, 0, lab, '', [])



