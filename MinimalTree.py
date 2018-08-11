#[1,2,3,4,5,6]
#[1,2,3,4,5,6,7]
def minimalTree(arr):
    return minimalTreeHelper(arr, 0, len(arr) - 1)

def minimalTreeHelper(arr, startIndex, endIndex):
    if (startIndex > endIndex):
        return None

    middle = (startIndex + endIndex)//2
    node = Node(arr[middle])
    node.left = minimalTreeHelper(arr, startIndex, middle - 1)
    node.right = minimalTreeHelper(arr, middle + 1, endIndex)
    return node






