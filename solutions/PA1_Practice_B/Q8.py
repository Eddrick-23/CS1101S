def remove_subseq(L, start_pos, end_pos):

    # WRITE YOUR SOLUTION HERE.
    def helper(xs, curr_idx):
        if is_none(xs):
            return xs
        if start_pos <= curr_idx and curr_idx <= end_pos:
            return helper(tail(xs), curr_idx + 1)
        else:
            return pair(head(xs), helper(tail(xs), curr_idx + 1))
    
    return helper(L, 0) 
