def rc(price, n):
    T = [0] * (n + 1)
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            T[i] = max(T[i], price[j - 1] + T[i - j])
    return T[n] 
 
if __name__ == '__main__':
 
    # length = [1, 2, 3, 4, 5, 6, 7, 8]
    price = [1, 5, 8, 9, 10, 17, 17, 20]
    n = 4  # rod length
 
    print("Profit is", rc(price, n))