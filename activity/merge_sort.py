from .mergelib import merge_sorted

# Implement merge_sort
# merge_sorted is a helper function that merges 2
# already sorted lists in linear time and space
# with respect to the combined lengths of the lists.


def merge_sort(data):
    if len(data) < 2:
        return data

    middle = len(data) // 2

    return merge_sorted(merge_sort(data[:middle]), merge_sort(data[middle:]))
