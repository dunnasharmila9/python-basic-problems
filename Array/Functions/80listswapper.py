##80.1.List Element Swapper Write a function swap_elements(lst, pos1, pos2) that swaps elements at the given indices and returns the list.
def swap_elements(lst, pos1, pos2):

    lst[pos1], lst[pos2] = lst[pos2], lst[pos1]

    return lst


numbers = [10, 20, 30, 40, 50]

result = swap_elements(numbers, 1, 3)

print(result)
