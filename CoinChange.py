def findMinCoins(S, N):
    T = [0] * (N + 1)
    for i in range(1, N + 1):
        T[i] = float('inf')
        for c in range(len(S)):
            if i - S[c] >= 0:
                res = T[i - S[c]]
                if res != float('inf'):
                    T[i] = min(T[i], res + 1)
    return T[N]
 
 
if __name__ == '__main__':
 
    # n coins of given denominations
    S = [1, 2, 3, 4]
 
    # Total Change required
    N = 15
 
    coins = findMinCoins(S, N)
    if coins != float('inf'):
        print("Minimum number of coins required to get desired change is", coins)
 



