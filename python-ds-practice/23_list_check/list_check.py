def list_check(lst):
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """


    for i in lst:
        #return false if i is not a list
        if not isinstance(i, list):
            return False
    #if it never returned false, must all be a list
    return True
