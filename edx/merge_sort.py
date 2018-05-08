# merge sort algorithm
# devide and conquer

# both list must be sorted
def merge(left, right):
    """Merge left and right list"""
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        elif right[j] < left[i]:
            result.append(right[j])
            j += 1
        else: # both equal
            result.append(left[i])
            result.append(right[j])
            i += 1
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result

def merge_sort(L):
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L)//2
        left = merge_sort(L[:middle])
        right = merge_sort(L[middle:])
        print(left, right)
        return merge(left, right)

print(merge_sort([4,1,2,9,45,0,22,0]))
