def wordBreak(Dictionary, string, out=''):
    if not string:
        print(out)
        return
    for i in range(1, len(string) + 1):
        prefix = string[:i]
        if prefix in Dictionary:
            wordBreak(Dictionary, string[i:], out + " " + prefix)

if __name__ == '__main__':
    Dictionary  = [
        "self", "th", "is", "famous", "Word",
        "break", "b", "r", "e", "a", "k", "br",
        "bre", "brea", "ak", "problem"
    ]
    string = "Wordbreakproblem"

    wordBreak(Dictionary, string)
