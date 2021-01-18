def subsetSum(Array, n, sum):
    if sum == 0:
        return True
    if n < 0 or sum < 0:
        return False
    include = subsetSum(Array, n - 1, sum - Array[n])
    if include:
        return True
    exclude = subsetSum(Array, n - 1, sum)
    return exclude
def partition(Array):
 
    total = sum(Array)
    return (total & 1) == 0 and subsetSum(Array, len(Array) - 1, total/2)
 
 
if __name__ == '__main__':
    Array = [7, 3, 1, 5, 4, 8]
 
    print(partition(Array))