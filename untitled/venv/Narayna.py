
def next_permutation(lst):
    i = len(lst)-1
    while True:
        if i < 2:
            return False  # Нет больше перестановок
        if lst[i-1] < lst[i]:
            break
        i -= 1

    j = len(lst) - 1
    while j > i:
        if lst[j] > lst[i]:
            break


    return True