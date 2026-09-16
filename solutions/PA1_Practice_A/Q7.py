def eval_poly(poly):

    # WRITE YOUR SOLUTION HERE.
    # we need to turn each term/pair into a number for some x = value
    # then sum everything together
    # use reduce
    # but question wants us to return a function that expects the x value
    # so wrap in a lambda / function
    def evaluator(x): 
        return reduce(
            lambda p, acc: head(p) * math_pow(x, tail(p)) + acc,
            0,
            poly)
    
    return evaluator
