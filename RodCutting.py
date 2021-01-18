def rodCut(price, n):
    if n == 0:
        return 0 
    maxValue = float('-inf')
    for i in range(1, n + 1):
        cost = price[i - 1] + rodCut(price, n - i)
        if cost > maxValue:
            maxValue = cost 
    return maxValue
 
if __name__ == '__main__':
    price = [1, 5, 8, 9, 10, 17, 17, 20]
    n = 4
    print("Profit is", rodCut(price, n))
