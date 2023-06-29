MAX_LOAD = 20


def divide_items(items: list) -> list:
    """
    Divide items into batches.
    Each batch can contain max 2 items.
    Arrange items into batches that don't excess MAX_LOAD.
    The goal is to create the least possible number of batches.
    
    :param items: List of items' weights
    :return: List of 1- or 2-element tuples
    """
    items.sort()
    result = []
    while len(items) > 1:
        if items[0] + items[-1] <= MAX_LOAD:
            result.append((items.pop(0), items.pop()))
        else:
            result.append((items.pop(),))
    else:
        if len(items) == 1:
            result.append((items[0],))
    return result
