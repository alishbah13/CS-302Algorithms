def MatrixChainMultiplication(dims, i, j, T):
    if j <= i + 1:
        return 0
    min = float('inf')
    if T[i][j] == 0:
 
        """
            (M[i+1]) x (M[i+2]..................M[j])
            (M[i+1]M[i+2]) x (M[i+3.............M[j])
            ...
            ...
            (M[i+1]M[i+2]............M[j-1]) x (M[j])
        """
 
        for k in range(i + 1, j):
            cost = MatrixChainMultiplication(dims, i, k, T)
            cost += MatrixChainMultiplication(dims, k, j, T)
            cost += dims[i] * dims[k] * dims[j]
            if cost < min:
                min = cost
 
        T[i][j] = min
    return T[i][j] 
 
if __name__ == '__main__':
    dims = [10, 30, 5, 60]
    T = [[0 for x in range(len(dims))] for y in range(len(dims))]
 
    print("Minimum cost is", MatrixChainMultiplication(dims, 0, len(dims) - 1, T))