def make_NiFT(T):

    # WRITE YOUR SOLUTION HERE.
    # filter out every number
    # filter out every list
    # recurse on every list element
    # append both such that numbers in front
    if is_none(T):
        return None
    
    numbers_only = filter(lambda x: is_number(x), T)
    llist_only = filter(lambda x: is_llist(x), T)
    nift_rest = map(lambda xs: make_NiFT(xs), llist_only)
    return append(numbers_only, nift_rest)
