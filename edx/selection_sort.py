# selection sort algorithm
# little more efficient than bubble sort
def selection_sort(L):
    suffixSt = 0
    while suffixSt != len(L):
        for i in range(suffixSt, len(L)):
            if L[i] < L[suffixSt]:
                (L[i], L[suffixSt]) = (L[suffixSt], L[i])
        suffixSt += 1
    return L

print(selection_sort([2, 5, 6, 1, 8, 22, 0]))
