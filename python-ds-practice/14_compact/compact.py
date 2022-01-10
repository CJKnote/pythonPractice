def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """
    newList = []

    for item in lst:
        #if item is true, it will add
        if item:
            newList.append(item)

    return newList
