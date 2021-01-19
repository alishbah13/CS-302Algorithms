def subsetSum(A, n, sum):
    T = [[False for x in range(sum + 1)] for y in range(n + 1)]
    for i in range(n + 1):
        T[i][0] = True
    for i in range(1, n + 1):
        for j in range(1, sum + 1):
            if A[i - 1] > j:
                T[i][j] = T[i - 1][j]
            else:
                T[i][j] = T[i - 1][j] or T[i - 1][j - A[i - 1]]
 
    return T[n][sum]
 
def partition(A):
    total = sum(A)
    return (total & 1) == 0 and subsetSum(A, len(A), total // 2)
 
 
if __name__ == '__main__':
 
    # Input: set of items
    A = [7, 3, 1, 5, 4, 8]
 
    if partition(A):
        print("Yes")
    else:
        print("No")