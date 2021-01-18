def dist(str1, m, str2, n):
    if m == 0:
        return n 
    if n == 0:
        return m

    cost = 0 if (str1[m - 1] == str2[n - 1]) else 1 
    return min(dist(str1, m - 1, str2, n) + 1,            # deletion (case 3a))
               dist(str1, m, str2, n - 1) + 1,            # insertion (case 3b))
               dist(str1, m - 1, str2, n - 1) + cost)     # substitution (case 2 + 3c)
 
if __name__ == '__main__':
 
    str1 = "kitten"
    str2 = "sitting"
    print("The Levenshtein Distance is", dist(str1, len(str1), str2, len(str2)))