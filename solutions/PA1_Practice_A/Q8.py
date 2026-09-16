def add_poly(poly1, poly2):
    if is_none(poly1):

        # WRITE YOUR SOLUTION HERE.
        return poly2

    elif is_none(poly2):

        # WRITE YOUR SOLUTION HERE.
        return poly1

    else:
        coeff1 = head(head(poly1))
        coeff2 = head(head(poly2))
        exp1 = tail(head(poly1))
        exp2 = tail(head(poly2))

        if exp1 == exp2:

            # WRITE YOUR SOLUTION HERE.
            # powers match, so merge to one term
            # take care of case where coefficients add to 0
            # we drop the term
            if coeff1 + coeff2 == 0:
                return add_poly(tail(poly1), tail(poly2))
            else:
                return pair(
                        pair(coeff1 + coeff2, exp1), 
                        add_poly(tail(poly1), tail(poly2))
                    )

        elif exp1 < exp2:

            # WRITE YOUR SOLUTION HERE.
            # 1 has smaller power, so we take term from poly1
            # leave term from poly2
            return pair(pair(coeff1, exp1), add_poly(tail(poly1), poly2)) 

        else:

            # WRITE YOUR SOLUTION HERE.
            # 2 has smaller power, so we take term from poly2
            # leave term from poly1
            return pair(pair(coeff2, exp2), add_poly(poly1, tail(poly2))) 
