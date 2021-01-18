def LCS(X, Y, m, n, lookup):
    
    if m == 0 or n == 0:
        return 0
    key = (m, n)
    if key not in lookup:

        if X[m - 1] == Y[n - 1]:
            lookup[key] = LCS(X, Y, m - 1, n - 1, lookup) + 1 
        else:
            lookup[key] = max(LCS(X, Y, m, n - 1, lookup),
                              LCS(X, Y, m - 1, n, lookup))

    return lookup[key]

def SCSLength(X, Y, m, n, lookup):
    if m == 0 or n == 0:
        return n + m
 
    key = (m, n)

    if key not in lookup:
        if X[m - 1] == Y[n - 1]:
            lookup[key] = SCSLength(X, Y, m - 1, n - 1, lookup) + 1
        else:
            lookup[key] = min(SCSLength(X, Y, m, n - 1, lookup),
                              SCSLength(X, Y, m - 1, n, lookup)) + 1
    return lookup[key]

def dist(X, Y):
 
    (m, n) = (len(X), len(Y))
    T = [[0 for x in range(n + 1)] for y in range(m + 1)]
    for i in range(1, m + 1):
        T[i][0] = i                     
 
    for j in range(1, n + 1):
        T[0][j] = j                     
 
    for i in range(1, m + 1):
 
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:    
                cost = 0                
            else:
                cost = 1                
 
            T[i][j] = min(T[i - 1][j] + 1,          # deletion (case 3b)
                          T[i][j - 1] + 1,          # insertion (case 3a)
                          T[i - 1][j - 1] + cost)   # replace (case 2 + 3c)
    return T[m][n]

def LIS(A):
    L = [0] * len(A)
    L[0] = 1
    for i in range(1, len(A)):
        for j in range(i):
            if A[j] < A[i] and L[j] > L[i]:
                L[i] = L[j]
 
        L[i] = L[i] + 1
    return max(L)

def MCM(dims):
 
    n = len(dims)

    c = [[0 for x in range(n + 1)] for y in range((n + 1))]
 
    for length in range(2, n + 1): 
        for i in range(1, n - length + 2):
            j = i + length - 1
            c[i][j] = float('inf')
            k = i
            while j < n and k <= j - 1:
                cost = c[i][k] + c[k + 1][j] + dims[i - 1] * dims[k] * dims[j]
                if cost < c[i][j]:
                    c[i][j] = cost
                k = k + 1
 
    return c[1][n - 1]

def KS(v, w, W):

    T = [[0 for x in range(W + 1)] for y in range(len(v) + 1)]
    for i in range(1, len(v) + 1):
        for j in range(W + 1):
            if w[i - 1] > j:
                T[i][j] = T[i - 1][j]
            else:
                T[i][j] = max(T[i - 1][j], T[i - 1][j - w[i - 1]] + v[i - 1])

    return T[len(v)][W]