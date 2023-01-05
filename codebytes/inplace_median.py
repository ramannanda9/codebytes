import bisect
from typing import List, Union


def get_median(elements:List[int], size:int) -> float:
    if size % 2 == 0:
        return (elements[size // 2] + elements[size // 2 - 1]) / 2
    else:
        return elements[size // 2]

def inplace_median(numbers: List[int], window_size:int)->List[Union[float,int]]:
    """
    Gives a list of medians in place
    :param numbers:
    :param window_size:
    :return:
    """
    medians=[]
    current_window=[]
    first_sort=False
    if numbers is None or len(numbers)<window_size:
        return []
    for idx, number in enumerate(numbers):
        if idx<window_size:
            current_window.append(number)
        else:
            if not first_sort:
                current_window.sort()
            median=get_median(current_window, window_size)
            medians.append(median)
            number_to_delete=numbers[idx-window_size]
            idx_to_delete=bisect.bisect_left(current_window, number_to_delete)
            current_window.pop(idx_to_delete)
            idx_to_insert=bisect.bisect_right(current_window, number)
            current_window.insert(idx_to_insert, number)
    medians.append(get_median(current_window, window_size))
    return medians








