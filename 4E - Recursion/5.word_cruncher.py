def find_all_solutions(idx, target_word, words_by_idx, words_count, used_words):
    if idx >= len(target_word):     # дъно на рекурсията
        print(' '.join(used_words))
        return

    if idx not in words_by_idx:
        return

    for word in words_by_idx[idx]:
        if words_count[word] == 0:      # нямам дума, която мога да сложа на този индекс
            continue

        used_words.append(word)     # добавяме всяка дума
        words_count[word] -= 1

        find_all_solutions(idx + len(word), target_word, words_by_idx, words_count, used_words)

        used_words.pop()    # backtracking  махаме думата, след кочто няма подходяща, че да продължим
        words_count[word] += 1


words = input().split(', ')
target_word = input()
words_by_idx = {}
words_count = {}

for word in words:
    if word in words_count:
        words_count[word] += 1
        continue

    words_count[word] = 1

    try:
        idx = 0
        while True:
            idx = target_word.index(word, idx)   # 'word'.index('rd') --> 2

            if idx not in words_by_idx:
                words_by_idx[idx] = []
            words_by_idx[idx].append(word)
            idx += len(word)
    except ValueError:
        pass

find_all_solutions(0, target_word, words_by_idx, words_count, [])
