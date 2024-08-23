def reverse_array(idx, elements):
    if idx == len(elements) // 2:  # base case
        return

    swap_idx = len(elements) - 1 - idx  
    elements[idx], elements[swap_idx] = elements[swap_idx], elements[idx]  # pre-action
    reverse_array(idx + 1, elements)  # recursive call


elements = input().split()
reverse_array(0, elements)
print(*elements)

###########################################################################
# interactive solution is better:
elements = input().split()

for left_idx in range(len(elements) // 2):
    right_idx = len(elements) - 1 - left_idx
    elements[left_idx], elements[right_idx] = elements[right_idx], elements[left_idx]
print(*elements)

#########################################################


def reverse_array(array, reversed_array):
    if not array:   # base case
        print(' '.join(reversed_array))
        return

    
    reversed_array.append(array.pop(-1))  # pre-action
    
    reverse_array(array, reversed_array)  # recursive call


array = [x for x in input().split(' ')]
reverse_array(array, [])



#########################################################



def reverse_array(idx, array):
    if idx == len(array) // 2:
        return print(' '.join(array))

    array[idx], array[-idx - 1] = array[-idx - 1], array[idx]

    reverse_array(idx + 1, array)


array = [x for x in input().split(' ')]
reverse_array(0, array)
