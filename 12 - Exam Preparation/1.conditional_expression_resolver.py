def parse_expression(expression, index):     # using recursion
    if expression[index].isdigit():   # дъно на рекурсията
        return expression[index]

    if expression[index] == 't':
        return parse_expression(expression, index + 2)

    cursor = index + 2
    conditional_statements_counter = 0
    while True:
        symbol = expression[cursor]
        if symbol == '?':
            conditional_statements_counter += 1
        elif symbol == ':':
            if conditional_statements_counter == 0:
                return parse_expression(expression, cursor + 1)
            conditional_statements_counter -= 1
        cursor += 1


expression = input().split()
print(parse_expression(expression, 0))

#################################################################################################################

import re

expression = input()
pattern = r'([tf]\s\?\s\d+\s\:\s\d+)'

while True:
    matches = re.findall(pattern, expression)
    if not matches:
        break

    condition, true_answer, false_answer = matches[0][0], matches[0][4], matches[0][-1]
    answer = true_answer if condition == 't' else false_answer
    expression = expression.replace(matches[0], answer)

print(expression)
