def SCS(str1, str2, len1, len2):
    if len1 == 0 or len2 == 0:
        return len1 + len2
    if str1[len1 - 1] == str2[len2 - 1]:
        return SCS(str1, str2, len1 - 1, len2 - 1) + 1
    return min(SCS(str1, str2, len1, len2 - 1) + 1, SCS(str1, str2, len1 - 1, len2) + 1)


if __name__ == '__main__':

    string1 = "ABCBDAB"
    string2 = "BDCABA"
    print("The length of shortest Common supersequence is", SCS(string1, string2, len(string1), len(string2)))
