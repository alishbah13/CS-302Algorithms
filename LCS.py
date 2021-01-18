
def LCS(String1, String2, len1, len2):   
    if len1 == 0 or len2 == 0:
        return 0
    if String1[len1 - 1] == String2[len2 - 1]:
        return LCS(String1, String2, len1 - 1, len2 - 1) + 1
    return max(LCS(String1, String2, len1, len2 - 1), LCS(String1, String2, len1 - 1, len2))


if __name__ == '__main__':
    String1 = "Fakhiha"
    String2 = "Alishbah"
    len1 = len(String1)
    len2 = len(String2)
    print("The length of Longest Common Sub Sequence  is : ", LCS(String1, String2, len1, len2))  