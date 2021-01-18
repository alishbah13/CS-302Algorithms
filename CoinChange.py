def findMinCoins(set, Change_Req):
    if Change_Req == 0:
        return 0
    if Change_Req < 0:   #if negative
        return float('inf')
    coins = float('inf')    #use @infinite num req
 
    for i in range(len(set)):
        res = findMinCoins(set, Change_Req - set[i])
        if res != float('inf'):
            coins = min(coins, res + 1)
    return coins
 
 
if __name__ == '__main__':
    set = [1, 3, 5, 7]
    Change_Req = 18
    coins = findMinCoins(set, Change_Req)
    if coins != float('inf'):
        print("Minimum number of coins required to get desired change is", coins)
