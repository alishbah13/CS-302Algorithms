def LIS(A, n, i=0, prev=float('-inf')):
    if i == n:
        return 0
    excl = LIS(A, n, i + 1, prev)
    incl = 0
    if A[i] > prev:
        incl = 1 + LIS(A, n, i + 1, A[i])
    return max(incl, excl)
    
if __name__ == '__main__':

    A = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]

    print("Length of LIS is", LIS(A, len(A)))