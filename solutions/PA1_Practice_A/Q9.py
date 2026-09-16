# Question 9

# You may write helper functions here.


def is_prefix_of(subseq, seq):

    # WRITE YOUR SOLUTION HERE.
    # at matching index/rank, the corresponding values for
    # subseq and seq must match
    # we reach base case i.e. is prefix, when subseq is None
    # remember to handle other cases where seq may be shorter than subseq
    
    if subseq is None:
        return True
    if seq is None:
        return False
    
    if head(subseq) != head(seq):
        return False
    else:
        return is_prefix_of(tail(subseq), tail(seq))
    
    