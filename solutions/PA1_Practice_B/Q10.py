def flatten_bin_tree(T):

    # WRITE YOUR SOLUTION HERE.
    # we represent a tree "node" as
    # llist(node_val, left_subtree, right_subtree)
    # we are guaranteed node_val is just a number
    # while left and right_subtree are lists
    # to build flattened tree
    # want
    # llist(flattened_left_subtree_elements, node_val, flattened_right_subtree elements)
    
    if is_none(T):
        return None
    
    node_val = head(T)
    flattened_left = flatten_bin_tree(llist_ref(T, 1))
    flattened_right = flatten_bin_tree(llist_ref(T, 2))
    return append(flattened_left, pair(node_val, flattened_right))
