def max_list_iter(int_list):  # must use iteration not recursion
    """finds the max of a list of numbers and returns the value (not the index)
  If int_list is empty, returns None. If list is None, raises ValueError"""

    if int_list is None:
        raise ValueError

    if not int_list:
        return None

    if len(int_list) == 1:
        return int_list[0]

    max_so_far: object = int_list[0]
    for i in range(len(int_list)):
        if int_list[i] > max_so_far:
            max_so_far = int_list[i]

    return max_so_far


def reverse_rec(int_list):  # must use recursion
    """recursively reverses a list of numbers and returns the reversed list
   If list is None, raises ValueError"""
    if int_list is None:
        raise ValueError

    if not int_list:
        return []

    if len(int_list) == 1:
        return int_list

    return reverse_rec(int_list[1:]) + [int_list[0]]


def bin_search(target, low, high, int_list):  # must use recursion
    """searches for target in int_list[low..high] and returns index if found
   If target is not found returns None. If list is None, raises ValueError """
    if int_list is None:
        raise ValueError

    if not int_list:
        return None

    if len(int_list) == 1:
        if int_list[0] == target:
            return 0
        else:
            return None

    if len(int_list[low:high]) > 1:
        mid = 1 + int(high - 1 / 2)  # In order to get the middle value
        if int_list[mid] == target:  # Checks if the middle value matches the target
            return mid  # returns the index, not the value
        elif int_list[mid] < target:  # Checks if the mid value is less than the target
            # so that we can then decide whether to ignore the first half or the second
            # half
            return bin_search(target, mid + 1, high, int_list)
        else:  # If the mid value is greater than the target, then
            return bin_search(target, low, mid - 1, int_list)
    else:
        return None  # If target isn't found in the list, this makes sure to
        # return None, since the only way to get to the else statement is
        # to not have triggered any of the other bits of code that
