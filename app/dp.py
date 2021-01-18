def LCS(X, Y, m, n, lookup):
    
 
    # return if we have reached the end of either string
    if m == 0 or n == 0:
        return 0
 
    # construct a unique dict key from dynamic elements of the input
    key = (m, n)
 
    # if sub-problem is seen for the first time, solve it and
    # store its result in a dict
    if key not in lookup:
 
        # if last character of X and Y matches
        if X[m - 1] == Y[n - 1]:
            lookup[key] = LCS(X, Y, m - 1, n - 1, lookup) + 1
 
        else:
            # else if last character of X and Y don't match
            lookup[key] = max(LCS(X, Y, m, n - 1, lookup),
                              LCS(X, Y, m - 1, n, lookup))
 
    # return the sub-problem solution from the dictionary
    return lookup[key]
 