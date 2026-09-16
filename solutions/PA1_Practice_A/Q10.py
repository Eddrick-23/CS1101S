def subseq_replace(new_sub, old_sub, seq):

    # WRITE YOUR SOLUTION HERE.
    # we check if a prefix matches
    # no prefix, then move down seq by one
    # if prefix, then we tail length(old_sub) times and append new_sub infront
    # repeat until we reach the end
    
    if is_none(seq): # base case
        return None
        
    if is_prefix_of(old_sub, seq):
        wish = subseq_replace(new_sub, old_sub, tail_n_times(seq, length(old_sub)))
        return append(new_sub, wish)
    else:
        return pair(head(seq), subseq_replace(new_sub, old_sub, tail(seq)))
