def wordBreak(dict, str, lookup):
    n = len(str)
    if n == 0:
        return True
    if lookup[n] == -1:
        lookup[n] = 0 
        for i in range(1, n + 1):
            prefix = str[:i]
            if prefix in dict and wordBreak(dict, str[i:], lookup):
                lookup[n] = 1
                return True
    return lookup[n] == 1
 
 
if __name__ == '__main__':
    dict = ["self", "th", "is", "famous", "Word",
            "break", "b", "r", "e", "a", "k", "br",
            "bre", "brea", "ak", "problem"]
    str = "Wordbreakproblem"
    lookup = [-1] * (len(str) + 1)
 
    if wordBreak(dict, str, lookup):
        print("String can be segmented")
    else:
        print("String can't be segmented")
 