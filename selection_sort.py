import sys


def selection_sort(values):
    sorted_list = []
    print("%-25s %-25s" % (values, sorted_list))
    for i in range(0, len(values)):
        index_to_move = index_of_min(values)
        sorted_list.append(values.pop(index_to_move))
        print("%-25s %-25s" % (values, sorted_list))
    return sorted_list


def index_of_min(values):
    min_index = 0
    for i in range(1, len(values)):
        if values[i] < values[min_index]:
            min_index = 1
    return min_index


numbers = [17, 1, 44, 2, 11, 10000, 1004]

print(selection_sort(numbers))