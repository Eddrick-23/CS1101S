def insert_subseq(L, pos, S):
    # WRITE YOUR SOLUTION HERE.
    if pos == 0:
        return append(S, L)
    else:
        return pair(head(L), insert_subseq(tail(L), pos - 1, S))
