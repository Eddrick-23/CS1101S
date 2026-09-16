def is_interleaving(A, B, C):
    # WRITE YOUR SOLUTION HERE.
    # if both match take from either
    # if one match take from that side only
    # if none match, return False
    if is_none(C):
        return True
    if not is_none(A) and head(A) == head(C) and not is_none(B) and head(B) == head(C):
        return is_interleaving(tail(A), B, tail(C)) or is_interleaving(A, tail(B), tail(C))
    elif not is_none(A) and head(A) == head(C):
        return is_interleaving(tail(A), B, tail(C))
    elif not is_none(B) and head(B) == head(C):
        return is_interleaving(A, tail(B), tail(C))
    else: 
        return False
